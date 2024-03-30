import openai
#==========================================openai 問答==================================
def fetch_openai_response(api_key, question):
    """
    使用OpenAI API发送聊天消息并获取回复。
    :param api_key: 用于身份验证的OpenAI API密钥。
    :param question: 用户的问题字符串。
    :return: 返回OpenAI聊天模型的回复内容。
    """
    regular = """丟規則"""

    # 设置OpenAI API密钥
    openai.api_key = api_key

    # 创建聊天会话并发送问题
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": regular},
            {"role": "user", "content": question}
        ]
    )

    # 提取并返回assistant的消息内容
    return response.choices[0].message['content']
#=============================================================================