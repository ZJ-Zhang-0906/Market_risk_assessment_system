from openai import OpenAI
import json 
#==========================================openai 問答==================================
def fetch_openai_response(api_key, question):
    """
    使用OpenAI API发送聊天消息并获取回复。
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
                用繁體中文回答顯示計算過程並簡短回答""" #TODO 不知道有沒有淦用 20240601 zj
    
    
    client = OpenAI(api_key=api_key)
    completion = client.chat.completions.create(
         model="gpt-4o",
         messages=[
                    {"role": "system", "content": regular},
                    {"role": "user", "content": question}
                ]
                                                )

    respon=completion.choices[0].message.content
    response_json = {
        "response": respon
    }
    # print(respon)
    with open (r'C:\xampp\htdocs\Market_risk_assessment_system\DarkJoe\respon.json', 'w', encoding='utf-8') as f: #json 更換檔案儲存位置
        json.dump(response_json, f, ensure_ascii=False, indent=4)

    return respon

#=============================================================================

# print(fetch_openai_response('your_api_key','你好')) #test用



