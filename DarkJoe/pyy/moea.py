import requests
import json
import pymysql
import pymysql.cursors
from connet_db import connect



def fetch_data_and_insert_to_py_moea_input():
    # 建立資料庫連接
    conn, driver = connect()
    cursor = conn.cursor()

    
    try:
        # 索引最新的資料表記錄
        sql = "SELECT * FROM web_input ORDER BY AutoNO DESC LIMIT 1"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)

        # 選擇最新記錄的統一編號
        sql = "SELECT BusinessAccountingNO FROM web_input ORDER BY AutoNO DESC LIMIT 1"
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result[0])

        # 使用獲得的統一編號向API請求資料
        key = result[0]
        url = f"https://data.gcis.nat.gov.tw/od/data/api/5F64D864-61CB-4D0D-8AD9-492047CC1EA6?$format=json&$filter=Business_Accounting_NO eq {key}&$skip=0&$top=1"
        web = requests.get(url)
        data = json.loads(web.text)
        # print("抓到了?")

        # 插入獲得的資料到資料庫
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

    except Exception as e:
        print(f"發生錯誤：{e}")

    finally:
        # 關閉資料庫連接
        cursor.close()
        conn.close()

    print("資料已成功插入到資料庫，並為 web_input 表添加了索引。")


# fetch_data_and_insert_to_py_moea_input()