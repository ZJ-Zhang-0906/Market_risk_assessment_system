from openai import OpenAI
import json 
#==========================================openai 問答==================================
def fetch_openai_response(api_key, questio):
    """
    使用OpenAI API发送聊天消息并获取回复。
    :param api_key: 用于身份验证的OpenAI API密钥。
    :param question: 用户的问题字符串。
    :return: 返回OpenAI聊天模型的回复内容。
    """
 
 
 
 
    regular = """ 資本額變動：
                    若近一年內增加，加一分。
                    若近一年內減少，扣一分。
                    地址變更：
                    若變更，扣一分。
                    若無變更，不加分也不扣分。
                    負責人變更：
                    若變更，扣一分。
                    若無變更，不加分也不扣分。
                    開發票狀況：
                    若近一年內有開發票，加一分。
                    若近一年內未開發票，扣一分。
                    營業狀況：
                    若近一年內有營業，加一分。
                    若近一年內無營業，扣一分。
                    訴訟狀況：
                    若近三年內有訴訟，扣一分。
                    若近三年內無訴訟，加一分。
                    勞基法違規：
                    若近三年內有罰款，扣一分。
                    若近三年內無罰款，加一分。
                    環保違規：
                    若近一年內有裁罰，扣一分。
                    若近一年內無裁罰，加一分。
                    動產設定：
                    若有動產設定，扣一分。
                    若無動產設定，加一分。
                    紀錄缺乏：
                    無相關數據紀錄視為無記錄。
                    風險分級：
                    最高7分
                    0分以下及1分：高風險。
                    2分及3分：中高風險。
                    4分及5分：中低風階。
                    6分及7分：低風險。"""   #TODO 不知道有沒有淦用 20240601 zj
    # regular = """資本額若有增加就加分若減少就扣一分（近一年）
    #             地址變更就扣一分若沒變更就不扣分也不加分
    #             負責人變更就扣一分若沒變更就不扣分也不加分
    #             未開發票就扣一分若有開發票就加一分（近一年）
    #             營業中加一分若沒有營業中就扣一分（近一年）
    #             有訴訟扣一分若沒有則加一分（近三年）
    #             勞基法有罰款就扣一分若沒有就加一分（近三年）
    #             環保有裁罰就扣一分若沒有就加一分（近一年）
    #             有動產設定就扣一分若沒有就加一分
    #             並且無資料視為無紀錄
    #             0分以下以及1分為高風險
    #             2分及3分為中高風險
    #             4分及5分為中低風險
    #             6分及7分為低風險
    #             用繁體中文回答並簡短回答""" #TODO 不知道有沒有淦用 20240601 zj
    
    
    client = OpenAI(api_key=api_key)
    completion = client.chat.completions.create(
         model="gpt-4-turbo",
         messages=[
                    {"role": "system", "content": regular},
                    {"role": "user", "content": questio}
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

# print(fetch_openai_response('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','你好'))



