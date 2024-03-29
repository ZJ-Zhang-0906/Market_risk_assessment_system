import requests
import json
import pymysql
import pymysql.cursors


# 資料庫連接設定
host = 'localhost'
user = 'root'
password = ''
db = 'fmras_sql'

# 建立連接
conn = pymysql.connect(host=host, user=user,
                       password=password, database=db, charset='utf8mb4')
cursor = conn.cursor()
# 索引資料表資料
try:
    # 編寫SQL查詢，假設資料表名為your_table_name
    sql = "SELECT * FROM web_input ORDER BY AutoNO DESC LIMIT 1"
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)

    # 修改這裡來選擇最新的記錄數量
    sql = "SELECT BusinessAccountingNO FROM web_input ORDER BY AutoNO DESC LIMIT 1"

    # 執行查詢
    cursor.execute(sql)

    # 獲取結果
    result = cursor.fetchone()  # 使用fetchone()獲取單條記錄，或使用fetchall()獲取所有結果

    print(result[0])


except:
    ...
# cursor.close()
# conn.close()
# API 請求
key = result[0]
url = f"https://data.gcis.nat.gov.tw/od/data/api/5F64D864-61CB-4D0D-8AD9-492047CC1EA6?$format=json&$filter=Business_Accounting_NO eq {key}&$skip=0&$top=1"
web = requests.get(url)
data = json.loads(web.text)

cursor = conn.cursor()
# 插入資料
insert_query = """
INSERT INTO py_moea_input (BusinessAccountingNO, CompanyStatusDesc, CompanyName, CapitalStockAmount, PaidInCapitalAmount, ResponsibleName, CompanyLocation)
VALUES (%s, %s, %s, %s, %s, %s, %s);
"""

for company in data:
    cursor.execute(insert_query, (company['Business_Accounting_NO'], company['Company_Status_Desc'], company['Company_Name'],
                   company['Capital_Stock_Amount'], company['Paid_In_Capital_Amount'], company['Responsible_Name'], company['Company_Location']))
    print(f"統一編號：{company['Business_Accounting_NO']}")
    print(f"公司狀況：{company['Company_Status_Desc']}")
    print(f"公司名稱：{company['Company_Name']}")
    print(f"資本總額(元)：{company['Capital_Stock_Amount']}")
    print(f"實收資本額(元):{company['Paid_In_Capital_Amount']}")
    print(f"代表人姓名：{company['Responsible_Name']}")
    print(f"公司所在地：{company['Company_Location']}")

# 提交並保存更改
conn.commit()

# 關閉資料庫連接
cursor.close()
conn.close()

print("資料已成功插入到資料庫，並為 web_input 表添加了索引。")
