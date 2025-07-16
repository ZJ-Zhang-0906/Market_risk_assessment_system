# 測試chrome driver 版本是否能支援瀏覽器
import pymysql
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from datetime import datetime, timedelta
from connet_db import connect
import json

def is_within_last_3_years(date_text):
    from datetime import datetime, timedelta
    current_date = datetime.now()
    date_obj = datetime.strptime(date_text, "%Y%m%d")
    three_years_ago = current_date - timedelta(days=3*365)
    return date_obj > three_years_ago

def fetch_data_and_insert_to_twincn():
    conn, driver = connect()
    cursor = conn.cursor()

    try:
        sql = "SELECT BusinessAccountingNO FROM web_input ORDER BY AutoNO DESC LIMIT 1"
        cursor.execute(sql)
        result = cursor.fetchone()
        if result:
            business_accounting_no = result[0]
            url = f"https://www.twincn.com/item.aspx?no={business_accounting_no}"
            driver.get(url)
            time.sleep(3)

            shareholder_info = ""
            lawsuit_info = "無資料"
            state = None
            use_unified_invoice = None
            company_name = None

            one_year_ago = datetime.now() - timedelta(days=365)
            sections = driver.find_elements(By.ID, 'page3')
            if sections:
                for section in sections:
                    items = section.find_elements(By.CLASS_NAME, 'resume-item')
                    for item in items:
                        month_title = item.find_element(By.TAG_NAME, 'h4').text
                        try:
                            month_date = datetime.strptime(month_title, '%Y年%m月')
                            if month_date >= one_year_ago:
                                uls = item.find_elements(By.TAG_NAME, 'ul')
                                for ul in uls:
                                    lis = ul.find_elements(By.TAG_NAME, 'li')
                                    for li in lis:
                                        shareholder_info += li.text + "; "
                        except ValueError:
                            continue
            else:
                print('未找到符合條件的 section')

            rows_page4 = driver.find_elements(By.CSS_SELECTOR, "#page4 .table-responsive tbody tr")
            if rows_page4:
                for row in rows_page4:
                    cells = row.find_elements(By.TAG_NAME, "td")
                    if cells and len(cells) > 1:
                        date_text = cells[0].text.strip()
                        try:
                            date = datetime.strptime(date_text, '%Y%m%d')
                            if datetime.now() - date <= timedelta(days=1095):
                                lawsuit_info = " ".join([div.text for div in cells[1].find_elements(By.CSS_SELECTOR, "div.col-sm-auto")])
                                break
                            if lawsuit_info == None:
                                lawsuit_info = "無資料"
                        except ValueError:
                            print(f"Date {date_text} format is incorrect. Skipping.")

            rows_page5 = driver.find_elements(By.CSS_SELECTOR, "#page5 .table-responsive tbody tr")
            for row in rows_page5:
                cells = row.find_elements(By.TAG_NAME, "td")
                if cells and len(cells) > 1:
                    header = cells[0].text.strip()
                    if header == "狀態":
                        state = cells[1].text.strip()
                    elif header == "使用統一發票":
                        use_unified_invoice = cells[1].text.strip()
                        use_unified_invoice = "有開統一發票" if use_unified_invoice == "是" else "無開統一發票"
                    elif header == "營業名稱":
                        company_name = cells[1].text.strip()
                    if state and use_unified_invoice and company_name:
                        break

            data = {
                "BusinessAccountingNO": business_accounting_no,
                "Lawsuit": lawsuit_info,
                "State": state or "無資料",
                "Use_unified_invoice": use_unified_invoice or "無資料",
                "CompanyName": company_name or "無資料",
                "Shareholder_info": shareholder_info or "無資料"
            }
            print(f"{data}插入成功")
            with open(f"{business_accounting_no}.json", "w", encoding="utf-8") as json_file:
                json.dump(data, json_file, ensure_ascii=False, indent=4)
                print(f"Data written to {business_accounting_no}.json")

        else:
            print("No BusinessAccountingNO found.")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()   
        cursor.close()
        conn.close()
# fetch_data_and_insert_to_twincn() #test調用

# ==========================================上面測試chrome driver 版本是否能支援瀏覽器============================================

#==========================================環境部爬汙染======================================== 
import requests
import time
from datetime import datetime, timedelta

# API金鑰設定
API_KEY = "your api key"



def test_api_connection():
    """
    🧪 測試API連線和API Key是否有效
    """
    url = "https://data.moenv.gov.tw/api/v2/DOC_P_17"
    params = {
        "format": "json",
        "limit": 1000,  # 只取1筆測試
        "api_key": API_KEY
    }
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    try:
        print("🧪 測試API連線...")
        response = requests.get(url, params=params, headers=headers, timeout=10)
        
        print(f"📊 HTTP狀態碼: {response.status_code}")
        print(f"📋 回應Headers: {dict(response.headers)}")
        
        if response.status_code == 200:
            try:
                data = response.json()
                print(f"✅ JSON解析成功")
                print(f"📝 回應格式: {type(data)}")
                print(f"🔑 回應keys: {list(data.keys()) if isinstance(data, dict) else 'Not a dict'}")
                print(f"📄 回應內容前100字符: {str(data)[:10000]}...")
                return True
            except Exception as e:
                print(f"❌ JSON解析失敗: {e}")
                print(f"📄 原始回應: {response.text[:200]}...")
                return False
        else:
            print(f"❌ API請求失敗")
            print(f"📄 錯誤回應: {response.text[:200]}...")
            return False
            
    except Exception as e:
        print(f"❌ 連線錯誤: {e}")
        return False
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


# 🔧 使用範例
if __name__ == "__main__":
    # 🎯 一鍵搞定：全撈 + 篩選 + 寫入資料庫
    result = fetch_data_and_insert_to_py_prtr_input()
    
    print(f"🎯 最終結果：{result}")
#=========================================================================================
# 調用函數


# fetch_company_by_uniform(86517510)