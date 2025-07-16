import sys
sys.stdout.reconfigure(encoding='utf-8')

import requests
from io import BytesIO
from openai import OpenAI
import os 
import time 
import json 

client = OpenAI(api_key='your api key')


def create_file(client, path):
    if path.startswith("http://") or path.startswith("https://"):
        response = requests.get(path)
        file_content = BytesIO(response.content)
        file_name = path.split("/")[-1]
        file_tuple = (file_name, file_content)
        upload_result = client.files.create(
            file=file_tuple,
            purpose="assistants"
        )
        print(f"已從 URL 上傳檔案: {file_name}")
        return upload_result.id

    elif os.path.isdir(path):
        files = []
        for filename in os.listdir(path):
            file_path = os.path.join(path, filename)
            if os.path.isfile(file_path):
                mod_time = os.path.getmtime(file_path)
                files.append((filename, file_path, mod_time))

        if not files:
            raise ValueError(f"資料夾 '{path}' 中沒有找到任何檔案")

        files.sort(key=lambda x: x[2], reverse=True)
        latest_filename, latest_filepath, mod_time = files[0]
        mod_time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(mod_time))
        print(f"找到最新檔案: {latest_filename} (最後修改於 {mod_time_str})")

        existing_files = client.files.list()
        for file in existing_files.data:
            if file.filename == latest_filename:
                print(f"檔案 {latest_filename} 已存在，跳過上傳")
                return file.id

        with open(latest_filepath, "rb") as file_content:
            upload_result = client.files.create(
                file=file_content,
                purpose="assistants"
            )
        print(f"已上傳最新檔案: {latest_filename} (ID: {upload_result.id})")
        return upload_result.id

    elif os.path.isfile(path):
        file_name = os.path.basename(path)
        existing_files = client.files.list()
        for file in existing_files.data:
            if file.filename == file_name:
                print(f"檔案 {file_name} 已存在，跳過上傳")
                return file.id

        with open(path, "rb") as file_content:
            upload_result = client.files.create(
                file=file_content,
                purpose="assistants"
            )
        print(f"已上傳檔案: {file_name} (ID: {upload_result.id})")
        return upload_result.id

    else:
        raise ValueError(f"指定的路徑 '{path}' 不是有效的檔案或資料夾")


def upload_and_create_vector_store(path):
    file_id = create_file(client, path)
    print("檔案 ID:", file_id)

    vector_store = client.vector_stores.create(
        name="knowledge_base"
    )
    print("向量儲存建立成功，Vector Store ID:", vector_store.id)

    file_upload_result = client.vector_stores.files.create(
        vector_store_id=vector_store.id,
        file_id=file_id
    )
    print("檔案加入向量儲存結果：", file_upload_result)

    print("等待檔案處理完成...")
    status = "processing"
    max_attempts = 30
    attempt = 0

    while status != "completed" and attempt < max_attempts:
        time.sleep(5)
        file_list_result = client.vector_stores.files.list(
            vector_store_id=vector_store.id
        )

        if hasattr(file_list_result, 'data') and len(file_list_result.data) > 0:
            status = file_list_result.data[0].status
            print(f"檢查狀態（第{attempt+1}次）: {status}")
            if status == "completed":
                print("向量存儲已準備就緒！")
                break

        attempt += 1

    return file_id, vector_store.id


def query_vector_store(vector_store_id, prompt):
    response = client.responses.create(
        model="gpt-4o-mini",
        input=prompt,
        tools=[{
            "type": "file_search",
            "vector_store_ids": [vector_store_id]
        }]
    )
    # print(response)

    if hasattr(response, 'output') and response.output:
        try:
            assistant_reply = response.output[-1].content[0].text
            print("\nAssistant 回應內容：")
            print(assistant_reply)
            return assistant_reply
        except (AttributeError, IndexError):
            print("找不到有效的回應內容。")
            return ""
    else:
        print("Assistant 沒有回應。")
        return ""


if __name__ == "__main__":
    import sys
    mode = sys.argv[1]  # "upload" 或 "ask"
    if mode == "upload":
        file_path = sys.argv[2]
        file_id, vector_id = upload_and_create_vector_store(file_path)
        print(f"{file_id}|{vector_id}")
    elif mode == "ask":
        vector_store_id = sys.argv[2]
        question = sys.argv[3]
        answer = query_vector_store(vector_store_id, question)
        print(answer)
