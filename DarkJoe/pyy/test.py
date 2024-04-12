import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from connet_db import connect



def is_within_last_3_years(date_text):
    # 此处替换为检查日期是否在过去三年内的逻辑
    from datetime import datetime, timedelta
    current_date = datetime.now()
    date_obj = datetime.strptime(date_text, "%Y%m%d")  # 假设日期文本是 YYYY-MM-DD 格式
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

            rows = driver.find_elements(By.CSS_SELECTOR, "#page4 .table-responsive tbody tr")
            if rows:
                found = False
                for row in rows:
                    cells = row.find_elements(By.TAG_NAME, "td")
                    if cells and len(cells) > 1:
                        date_text = cells[0].text.strip()
                        if is_within_last_3_years(date_text):
                            company_name = cells[1].find_element(By.CSS_SELECTOR, "a").text.strip()
                            lawsuit_info = " ".join([div.text for div in cells[1].find_elements(By.CSS_SELECTOR, "div.col-sm-auto")])

                            insert_sql = """
                                INSERT INTO twincn (BusinessAccountingNO, CompanyName, Lawsuit)
                                VALUES (%s, %s, %s);
                            """
                            cursor.execute(insert_sql, (business_accounting_no, company_name, lawsuit_info))
                            conn.commit()
                            print(f"Data inserted for {company_name}")
                            found = True
                            break
                        else:
                            print(f"Date {date_text} is not within the last 3 years. Skipping.")
                if not found:
                    print("No valid data found to insert.")
                    insert_sql = "INSERT INTO twincn (BusinessAccountingNO, CompanyName, Lawsuit) VALUES (0, 'No Data', 'No Data');"
                    cursor.execute(insert_sql)
                    conn.commit()
                    print("Inserted 0 into database for no valid data.")
            else:
                print("No rows found on the page.")
        else:
            print("No BusinessAccountingNO found.")

    except Exception as e:
        print(f"An error occurred: {e}")
        conn.rollback()
    finally:
        driver.quit()
        cursor.close()
        conn.close()

# 在這裡呼叫你的函數以運行程序
# fetch_data_and_insert_to_twincn()
# https://www.twincn.com/item.aspx?no={business_accounting_no}