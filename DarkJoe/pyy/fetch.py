import pymysql
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from datetime import datetime, timedelta
from connet_db import connect

# #==================================检查日期是否在过去三年内===========================================

def is_within_last_3_years(date_text):
    # 此处替换为检查日期是否在过去三年内的逻辑
    from datetime import datetime, timedelta
    current_date = datetime.now()
    date_obj = datetime.strptime(date_text, "%Y%m%d")  # 假设日期文本是 YYYY-MM-DD 格式
    three_years_ago = current_date - timedelta(days=3*365)
    return date_obj > three_years_ago
# #==================================================================================================

# #==================================台灣公司網爬訴訟==================================================

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

            # 从页面4抓取数据
            lawsuit_info = None
            rows_page4 = driver.find_elements(By.CSS_SELECTOR, "#page4 .table-responsive tbody tr")
            if rows_page4:
                for row in rows_page4:
                    cells = row.find_elements(By.TAG_NAME, "td")
                    if cells and len(cells) > 1:
                        date_text = cells[0].text.strip()
                        if is_within_last_3_years(date_text):
                            lawsuit_info = " ".join([div.text for div in cells[1].find_elements(By.CSS_SELECTOR, "div.col-sm-auto")])
                            print(f"Lawsuit Info: {lawsuit_info}")  # 调试输出诉讼信息
                            break
                        else:
                            print(f"Date {date_text} is not within the last 3 years. Skipping.")
            else:
                print("No rows found on page 4.")

            # 从页面5抓取数据
            state = None
            use_unified_invoice = None
            company_name = None
            
            rows_page5 = driver.find_elements(By.CSS_SELECTOR, "#page5 .table-responsive tbody tr")
            
            def process_rows(rows):
                nonlocal state, use_unified_invoice, company_name
                for row in rows:
                    cells = row.find_elements(By.TAG_NAME, "td")
                    if cells and len(cells) > 1:
                        header = cells[0].text.strip()
                        if header == "狀態":
                            state = cells[1].text.strip()
                        elif header == "使用統一發票":
                            use_unified_invoice = cells[1].text.strip()
                        elif header == "營業名稱":
                            company_name = cells[1].text.strip()
                        if state and use_unified_invoice and company_name:
                            break

            process_rows(rows_page5)

            # 插入数据库
            if lawsuit_info or state or use_unified_invoice or company_name:
                insert_sql = """
                    INSERT INTO twincn (BusinessAccountingNO, Lawsuit, state, Use_unified_invoice, CompanyName)
                    VALUES (%s, %s, %s, %s, %s);
                """
                cursor.execute(insert_sql, (business_accounting_no, lawsuit_info, state, use_unified_invoice, company_name))
                conn.commit()
                print(f"Data inserted for BusinessAccountingNO {business_accounting_no} with Lawsuit: {lawsuit_info}, state: {state}, Use_unified_invoice: {use_unified_invoice}, and CompanyName: {company_name}")
            else:
                print("No valid data found to insert.")
                insert_sql = "INSERT INTO twincn (BusinessAccountingNO, Lawsuit, state, Use_unified_invoice, CompanyName) VALUES (%s, %s, %s, %s, %s);"
                cursor.execute(insert_sql, (business_accounting_no, 'No Data', 'No Data', 'No Data', 'No Data'))
                conn.commit()
                print("Inserted 'No Data' into database for no valid data.")
        else:
            print("No BusinessAccountingNO found.")

    except Exception as e:
        print(f"An error occurred: {e}")
        conn.rollback()
    finally:
        driver.quit()
        cursor.close()
        conn.close()

#====================================================================================================

# fetch_data_and_insert_to_twincn()