from openai import OpenAI

import json

def fetch_openai_response( question):
    """
    使用OpenAI API发送聊天消息并获取回复，并将回复写入JSON文件。
    :param api_key: 用于身份验证的OpenAI API密钥。
    :param question: 用户的问题字符串。
    :return: 返回OpenAI聊天模型的回复内容。
    """
    regular = """資本額若有增加就加分若減少就扣一分（近一年）
                地址變更就扣一分若沒變更就不扣分也不加分
                負責人變更就扣一分若沒變更就不扣分也不加分
                未開發票就扣一分若有開發票就加一分（近一年）
                營業中加一分若沒有營業中就扣一分（近一年）
                有訴訟扣一分若沒有則加一分（近三年）
                勞基法有罰款就扣一分若沒有就加一分（近三年）
                環保有裁罰就扣一分若沒有就加一分（近一年）
                有動產設定就扣一分若沒有就加一分
                並且無資料視為無紀錄
                0分以下以及1分為高風險
                2分及3分為中高風險
                4分及5分為中低風險
                6分及7分為低風險
                用繁體中文回答"""
                
    result =OpenAI(api_key = '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')
    

    response = result.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": regular},
            {"role": "user", "content": question}
        ]
    )

    # 获取响应内容
    response_content = response.choices[0].message.content

    # 创建要写入JSON文件的数据对象
    response_json = {
        "response": response_content
    }

    # 将响应内容写入JSON文件
    with open(r'C:\xampp\htdocs\Market_risk_assessment_system\DarkJoe\respon.json', 'w', encoding='utf-8') as json_file:
        json.dump(response_json, json_file, ensure_ascii=False, indent=4)

    return response_content

# 测试函数
if __name__ == "__main__":
 
    question = "你好"
    response = fetch_openai_response( question)
    print(response)
