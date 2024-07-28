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


#==========================================環境部爬汙染======================================== 
def fetch_data_and_insert_to_py_prtr_input():
    conn, driver = connect()
    cursor = conn.cursor()
    try:
        today = datetime.now()
        last_year = today - timedelta(days=365)
        today_str = today.strftime("%Y-%m-%d")
        last_year_str = last_year.strftime("%Y-%m-%d")

        # 獲取最新的公司統一編號
        sql = "SELECT BusinessAccountingNO FROM web_input ORDER BY AutoNO DESC LIMIT 1"
        cursor.execute(sql)
        result = cursor.fetchone()  # 使用 fetchone() 獲取單條記錄
        business_accounting_no = result[0] if result else None
        if not business_accounting_no:
            print("No business accounting number found.")
            return

        driver_path = r'C:\xampp\htdocs\Market_risk_assessment_system\DarkJoe\pyy\chromedriver-win64\chromedriver.exe'
        service = Service(executable_path=driver_path)
        driver = webdriver.Chrome(service=service)
        driver.get("https://prtr.moenv.gov.tw/deal.html")

        # 輸入統一編號
        search_box = driver.find_element(By.NAME, "UniformNo")
        search_box.send_keys(business_accounting_no)

        # 輸入日期區間
        start_date_box = driver.find_element(By.XPATH, '//*[@id="wrap"]/div/div[1]/div[3]/div/div/div[1]/input')
        end_date_box = driver.find_element(By.XPATH, '//*[@id="wrap"]/div/div[1]/div[3]/div/div/div[3]/input')
        start_date_box.send_keys(last_year_str)
        end_date_box.send_keys(today_str)

        # 查詢公示案件按鈕
        button = driver.find_element(By.CLASS_NAME, "search_submit")
        button.click()
        time.sleep(2)

        try:  # 檢查是否有數據
            no_data_div = driver.find_element(By.CLASS_NAME, 'no_data')
            text = no_data_div.text
        except:  # 有數據
            have_data = driver.find_element(By.CLASS_NAME, 'result_number')
            text = have_data.text
            if any(char.isdigit() for char in text):
                text = "有環境裁罰"

        # 插入數據到數據庫
        insert_query = "INSERT INTO py_prtr_input (NumberOfData) VALUES (%s);"
        cursor.execute(insert_query, (text,))
        conn.commit()

    except Exception as e:
        print("An error occurred: ", e)
        conn.rollback()

    finally:
        time.sleep(0.5)  # 等待一些時間，以便查看搜索結果
        driver.quit()
        cursor.close()
        conn.close()

#=========================================================================================
# 調用函數

fetch_data_and_insert_to_py_prtr_input()