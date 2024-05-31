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
        # 從資料庫獲取最新的業務帳號
        sql = "SELECT BusinessAccountingNO FROM web_input ORDER BY AutoNO DESC LIMIT 1"
        cursor.execute(sql)
        result = cursor.fetchone()
        if result:
            business_accounting_no = result[0]
            url = f"https://www.twincn.com/item.aspx?no={business_accounting_no}"
            driver.get(url)
            time.sleep(3)

            # 初始化變數
            shareholder_info = ""
            lawsuit_info = "無資料"
            state = None
            use_unified_invoice = None
            company_name = None

            # 從頁面3獲取股東資料
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

            # 從頁面4抓取資料
            rows_page4 = driver.find_elements(By.CSS_SELECTOR, "#page4 .table-responsive tbody tr")
            if rows_page4:
                for row in rows_page4:
                    cells = row.find_elements(By.TAG_NAME, "td")
                    if cells and len(cells) > 1:
                        date_text = cells[0].text.strip()
                        try:
                            date = datetime.strptime(date_text, '%Y%m%d')
                            if datetime.now() - date <= timedelta(days=1095):  # 3年內
                                lawsuit_info = " ".join([div.text for div in cells[1].find_elements(By.CSS_SELECTOR, "div.col-sm-auto")])
                                break
                            if lawsuit_info == None:
                                lawsuit_info="無資料"
                        except ValueError:
                            print(f"Date {date_text} format is incorrect. Skipping.")

            # 從頁面5抓取資料
            rows_page5 = driver.find_elements(By.CSS_SELECTOR, "#page5 .table-responsive tbody tr")
            for row in rows_page5:
                cells = row.find_elements(By.TAG_NAME, "td")
                if cells and len(cells) > 1:
                    header = cells[0].text.strip()
                    if header == "狀態":
                        state = cells[1].text.strip()
                    elif header == "使用統一發票":
                        use_unified_invoice = cells[1].text.strip()
                        if use_unified_invoice == "是":
                            use_unified_invoice="有開統一發票"
                        else:
                            use_unified_invoice="無開統一發票"
                    elif header == "營業名稱":
                        company_name = cells[1].text.strip()
                    if state and use_unified_invoice and company_name:
                        break

            # 插入資料庫
            if lawsuit_info or state or use_unified_invoice or company_name or shareholder_info:
                insert_sql = """
                    INSERT INTO twincn (BusinessAccountingNO, Lawsuit, state, Use_unified_invoice, CompanyName, Change_money)
                    VALUES (%s, %s, %s, %s, %s, %s);
                """
                cursor.execute(insert_sql, (business_accounting_no, lawsuit_info, state, use_unified_invoice, company_name, shareholder_info))
                conn.commit()
                print(f"Data inserted for BusinessAccountingNO {business_accounting_no} with Lawsuit: {lawsuit_info}, state: {state}, Use_unified_invoice: {use_unified_invoice}, CompanyName: {company_name}, Shareholder_info: {shareholder_info}")
            else:
                print("No valid data found to insert.")
                insert_sql = "INSERT INTO twincn (BusinessAccountingNO, Lawsuit, state, Use_unified_invoice, CompanyName, Change_money) VALUES (%s, %s, %s, %s, %s, %s);"
                cursor.execute(insert_sql, (business_accounting_no, 'No Data', 'No Data', 'No Data', 'No Data', 'No Data'))
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