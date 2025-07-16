import os
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pymysql
from selenium.webdriver.chrome.service import Service
from connet_db import connect
from datetime import datetime, timedelta


# 连接数据库
#===========================================抓所有table資料並轉成json並過濾autono=================================
def fetch_and_clean_data():
    conn, driver = connect()
    cursor = conn.cursor()
    try:
        all_data = {}
        tables = ['py_prtr_input', 'py_moea_input', 'py_mol_input', 'py_ppstrq_input','twincn']

        with conn.cursor(pymysql.cursors.DictCursor) as cursor:
            for table in tables:
                cursor.execute(f"SELECT * FROM {table} ORDER BY AutoNo DESC LIMIT 1")
                result = cursor.fetchall()

                cleaned_result = []
                for row in result:
                    # 移除 'AutoNo' 字段
                    row.pop('AutoNo', None)
                    cleaned_result.append(row)

                all_data[table] = cleaned_result

        # 将所有数据转换为JSON格式
        json_data = json.dumps(all_data, ensure_ascii=False, indent=4)

        # 写入JSON文件
        file_path = r'C:\xampp\htdocs\Market_risk_assessment_system\DarkJoe\data.json'  #這是爬蟲所爬回來的資料 替换为你想要保存的路径
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(json_data)

        return json_data  # 返回文件路径
    finally:
        conn.close()
#============================================================================================


#==========================================環境部爬汙染======================================== 
# def fetch_data_and_insert_to_py_prtr_input():
#     conn, driver = connect()
#     cursor = conn.cursor()
#     try:
#         today = datetime.now()
#         last_year = today - timedelta(days=365)
#         today_str = today.strftime("%Y-%m-%d")
#         last_year_str = last_year.strftime("%Y-%m-%d")

#         # 獲取最新的公司統一編號
#         sql = "SELECT BusinessAccountingNO FROM web_input ORDER BY AutoNO DESC LIMIT 1"
#         cursor.execute(sql)
#         result = cursor.fetchone()  # 使用 fetchone() 獲取單條記錄
#         business_accounting_no = result[0] if result else None
#         if not business_accounting_no:
#             print("No business accounting number found.")
#             return

#         driver_path = r'C:\xampp\htdocs\Market_risk_assessment_system\DarkJoe\pyy\chromedriver-win64\chromedriver.exe' #這是chrome driver 的絕對路徑 替换为你想要保存的路径
#         service = Service(executable_path=driver_path)
#         driver = webdriver.Chrome(service=service)
#         driver.get("https://prtr.moenv.gov.tw/deal.html")

#         # 輸入統一編號
#         search_box = driver.find_element(By.NAME, "UniformNo")
#         search_box.send_keys(business_accounting_no)

#         # 輸入日期區間
#         start_date_box = driver.find_element(By.XPATH, '//*[@id="wrap"]/div/div[1]/div[3]/div/div/div[1]/input')
#         end_date_box = driver.find_element(By.XPATH, '//*[@id="wrap"]/div/div[1]/div[3]/div/div/div[3]/input')
#         start_date_box.send_keys(last_year_str)
#         end_date_box.send_keys(today_str)

#         # 查詢公示案件按鈕
#         button = driver.find_element(By.CLASS_NAME, "search_submit")
#         button.click()
#         time.sleep(2)

#         try:  # 檢查是否有數據
#             no_data_div = driver.find_element(By.CLASS_NAME, 'no_data')
#             text = no_data_div.text
#         except:  # 有數據
#             have_data = driver.find_element(By.CLASS_NAME, 'result_number')
#             text = have_data.text
#             if any(char.isdigit() for char in text):
#                 text = "有環境裁罰"

#         # 插入數據到數據庫
#         insert_query = "INSERT INTO py_prtr_input (NumberOfData) VALUES (%s);"
#         cursor.execute(insert_query, (text,))
#         conn.commit()

#     except Exception as e:
#         print("An error occurred: ", e)
#         conn.rollback()

#     finally:
#         time.sleep(0.5)  # 等待一些時間，以便查看搜索結果
#         driver.quit()
#         cursor.close()
#         conn.close()


import requests
import time
from datetime import datetime, timedelta

# API金鑰設定
API_KEY = "your api key"

def fetch_all_penalty_data():
    """
    🔄 全撈環境部裁罰資料
    回傳所有裁罰記錄的清單
    """
    url = "https://data.moenv.gov.tw/api/v2/DOC_P_17"
    all_records = []
    offset = 0
    limit = 1000  # 每次撈1000筆
    
    print(f"🔄 開始全撈環境部裁罰資料...")
    
    while True:
        params = {
            "format": "json",
            "limit": limit,
            "offset": offset,
            "api_key": API_KEY
        }
        
        # 🌐 添加headers模擬瀏覽器請求
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'zh-TW,zh;q=0.9,en;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive'
        }
        
        try:
            # 🔍 調試：印出完整請求資訊
            if offset == 0:
                print(f"🔗 請求URL: {url}")
                print(f"🔑 API Key: {API_KEY[:10]}...")
                print(f"📋 參數: {params}")
            
            response = requests.get(url, params=params, headers=headers, timeout=30)
            
            if response.status_code != 200:
                print(f"❌ HTTP狀態碼：{response.status_code}")
                print(f"⛔ 回應內容：{response.text[:500]}...")  # 只顯示前500字符
                if offset == 0:  # 第一次就失敗
                    return []
                break
                
            data = response.json()
            
            # 🔍 調試：印出API回應格式 (可在正式使用時移除)
            if offset == 0:  # 只在第一次請求時印出
                print(f"🔍 調試 - API回應格式：")
                print(f"   Total: {data.get('total', 'Unknown')}")
                print(f"   Keys: {list(data.keys())}")
                print(f"   Records count: {len(data.get('records', []))}")
            
            # 取得這批資料（環境部API的資料在'records'欄位）
            records = data.get('records', [])
            
            if not records:  # 沒有更多資料了
                print(f"📄 offset={offset} 沒有更多資料")
                break
                
            all_records.extend(records)
            print(f"📥 已撈取 {len(all_records)} 筆資料...")
            
            # 如果這批資料少於limit，表示已經撈完
            if len(records) < limit:
                print(f"✅ 已撈取完所有資料")
                break
                
            offset += limit
            
            # 加個延遲避免請求太頻繁
            time.sleep(0.1)
            
        except Exception as e:
            print(f"❌ 撈取資料時發生錯誤（offset={offset}）：{e}")
            break
    
    print(f"✅ 總共撈取 {len(all_records)} 筆裁罰資料")
    return all_records

def fetch_data_and_insert_to_py_prtr_input():
    """
    🎯 一鍵搞定：全撈環境部資料 + 篩選指定公司的一年內裁罰記錄 + 寫入資料庫
    (會自動從資料庫web_input表中撈取最新的CompanyName，並將結果寫入py_prtr_input)
    
    Returns:
        字串: "有環境裁罰" 或 "無環境裁罰"
    """
    
    # 🔗 連接資料庫
    conn, driver = connect()
    cursor = conn.cursor()
    
    try:
        # 🔍 撈取最新的CompanyName
        cursor.execute("SELECT CompanyName FROM web_input ORDER BY AutoNO DESC LIMIT 1")
        result = cursor.fetchone()
        company_name = result[0] if result else None
        
        if not company_name:
            print("❌ 找不到最新的 CompanyName")
            text = "無環境裁罰"
        else:
            print(f"📌 查詢公司：{company_name}")
            
            # 🔄 步驟1：全撈環境部裁罰資料
            print("🔄 開始全撈環境部裁罰資料...")
            all_records = fetch_all_penalty_data()
            
            if not all_records:
                print("⚠️ 無法取得裁罰資料")
                text = "無環境裁罰"
            else:
                # 📅 計算日期範圍（近一年）
                today = datetime.now()
                last_year = today - timedelta(days=365)
                
                print(f"📅 查詢期間：{last_year.strftime('%Y-%m-%d')} 至 {today.strftime('%Y-%m-%d')}")
                
                # 🔍 步驟2：篩選指定公司的記錄
                company_records = []
                
                for record in all_records:
                    # 檢查公司名稱是否符合（支援模糊比對）
                    record_name = record.get('name', '').strip()
                    if not record_name:
                        continue
                        
                    # 可以調整比對邏輯：完全相符或包含關係
                    if (company_name.lower() in record_name.lower() or 
                        record_name.lower() in company_name.lower()):
                        
                        # 檢查日期是否在一年內
                        record_time = record.get('time', '')
                        if record_time:
                            try:
                                # 處理不同的日期格式
                                for date_format in ['%Y-%m-%d', '%Y/%m/%d', '%Y-%m-%d %H:%M:%S']:
                                    try:
                                        record_date = datetime.strptime(record_time, date_format)
                                        break
                                    except ValueError:
                                        continue
                                else:
                                    continue  # 無法解析日期，跳過這筆
                                
                                if last_year <= record_date <= today:
                                    company_records.append(record)
                                    print(f"🎯 找到符合記錄：{record_name} - {record_time}")
                                    
                            except Exception as e:
                                print(f"⚠️ 日期解析錯誤：{record_time} - {e}")
                                continue
                
                # 📊 判斷結果
                if company_records:
                    print(f"⚠️ 一年內「{company_name}」有 {len(company_records)} 筆裁罰紀錄")
                    text = "有環境裁罰"
                else:
                    print(f"✅ 一年內「{company_name}」無裁罰紀錄")
                    text = "無環境裁罰"
        
        # ✍️ 寫入資料庫
        insert_sql = "INSERT INTO py_prtr_input (NumberOfData) VALUES (%s)"
        cursor.execute(insert_sql, (text,))
        conn.commit()
        print(f"✅ 寫入 py_prtr_input：{text}")
        
        return text
            
    except Exception as e:
        print(f"❌ 發生錯誤：{e}")
        conn.rollback()
        return "無環境裁罰"
        
    finally:
        # 🔐 關閉連線
        cursor.close()
        conn.close()
        driver.quit()

#=========================================================================================
# 調用函數

# fetch_data_and_insert_to_py_prtr_input()



# def fetch_data_and_insert_to_py_prtr_input():
#     conn, driver = connect()
#     cursor = conn.cursor()
#     try:
#         # 編寫SQL查詢，假設資料表名為your_table_name
#         sql = "SELECT * FROM web_input ORDER BY AutoNO DESC LIMIT 1"
#         cursor.execute(sql)
#         result = cursor.fetchall()
#         print(result)

#         # 修改這裡來選擇最新的記錄數量
#         sql = "SELECT BusinessAccountingNO FROM web_input ORDER BY AutoNO DESC LIMIT 1"

#         # 執行查詢
#         cursor.execute(sql)

#         # 獲取結果
#         result = cursor.fetchone()  # 使用fetchone()獲取單條記錄，或使用fetchall()獲取所有結果

#         print(result[0])

#     except:
#         ...

#     # 插入資料
#     insert_query = """
#     INSERT INTO py_prtr_input (NumberOfData)
#     VALUES (%s);
#     """

#     # 打開Google網頁
#     driver.get("https://prtr.moenv.gov.tw/deal.html")
#     # 找到搜尋框的元素
#     search_box = driver.find_element(By.NAME, "UniformNo")
#     # 在搜尋框中輸入關鍵字
#     search_box.send_keys(result[0])  # 83291953、81020420
#     # 查詢公示案件按鈕
#     button = driver.find_element(By.CLASS_NAME, "search_submit")
#     # 點擊按鈕
#     button.click()
#     time.sleep(2)
#     try:  # 沒有資料
#         no_data_div = driver.find_element(By.CLASS_NAME, 'no_data')
#         # 在no_data_div内部查找class为'text'的div
#         text_element = no_data_div.find_element(By.CLASS_NAME, 'text')
#         # 获取元素中的文本
#         text = text_element.text
#         if text=='0':
#             text = '沒有裁罰案件'
#         print(text)
#     except:  # 有資料
#         have_data = driver.find_element(By.CLASS_NAME, 'result_number')
#         text = have_data.text
#         if text == '1':
#             text = '有裁罰案件'
#         print(text)

#     try:
#         cursor.execute(insert_query, (text,))
#         conn.commit()
#     except pymysql.MySQLError as e:
#         print("Error in SQL execution: ", e)
#         conn.rollback()

#     # 等待一些時間，以便查看搜尋結果
#     time.sleep(1)

#     driver.quit()