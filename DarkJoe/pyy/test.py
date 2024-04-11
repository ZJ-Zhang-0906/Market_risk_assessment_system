import pymysql
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from datetime import datetime, timedelta
from connet_db import connect

# 检查日期是否在过去三年内
def is_within_last_3_years(date_str, date_format="%Y%m%d"):
    date_obj = datetime.strptime(date_str, date_format)
    three_years_ago = datetime.now() - timedelta(days=3*365)
    return date_obj >= three_years_ago

def fetch_data_and_insert_to_twincn():
    conn, driver = connect()
    cursor = conn.cursor()

    try:
        sql = "SELECT BusinessAccountingNO FROM web_input ORDER BY AutoNO DESC LIMIT 1"
        cursor.execute(sql)
        result = cursor.fetchone()
        if result:
            business_accounting_no = result[0]
            # 使用 BusinessAccountingNO 访问页面
            url = f"https://www.twincn.com/item.aspx?no={business_accounting_no}"
            driver.get(url)
            time.sleep(3)

            # 根据提供的HTML结构，找到所有的行
            rows = driver.find_elements(By.CSS_SELECTOR, "#page4 .table-responsive tbody tr")
            # 初始化已找到标志
            found = False
            for row in rows:
                cells = row.find_elements(By.TAG_NAME, "td")
                if cells and len(cells) > 1:
                    date_text = cells[0].text.strip()
                    # 检查日期是否在过去三年内
                    if is_within_last_3_years(date_text):
                        company_name = cells[1].find_element(By.CSS_SELECTOR, "a").text.strip()
                        lawsuit_info = " ".join([div.text for div in cells[1].find_elements(By.CSS_SELECTOR, "div.col-sm-auto")])

                        insert_sql = """
                            INSERT INTO twincn ( BusinessAccountingNO, CompanyName, Lawsuit)
                            VALUES (%s, %s, %s);
                        """
                        cursor.execute(insert_sql, ( date_text, company_name, lawsuit_info))
                        conn.commit()
                        print(f"Data inserted for {company_name}")
                        found = True
                        break
                    else:
                        print(f"Date {date_text} is not within the last 3 years. Skipping.")
                    if found:
                        break

    except Exception as e:
        print(f"An error occurred: {e}")
        conn.rollback()
    finally:
        driver.quit()
        cursor.close()
        conn.close()

# fetch_data_and_insert_to_twincn()
