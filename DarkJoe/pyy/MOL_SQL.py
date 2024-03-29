from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pymysql
from selenium.webdriver.chrome.service import Service
from connet_db import connect
import time
# 環境不 汙染
#-----------------------------------齊齊-2024-01-19-資料庫連接------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------
# 索引資料表資料
def fetch_data_and_insert_to_py_mol_input():
    conn, driver = connect()  # 使用connect函數來獲取連接和驅動器
    try:
        cursor = conn.cursor()
        
        # 獲取最新的公司名稱
        sql = "SELECT CompanyName FROM web_input ORDER BY AutoNO DESC LIMIT 1"
        cursor.execute(sql)
        result = cursor.fetchone()
        if result:
            company_name = result[0]
        else:
            print("No company name found.")
            return

        driver.get("https://announcement.mol.gov.tw/")
        search_box = driver.find_element(By.NAME, "UNITNAME")
        search_box.send_keys(company_name)
        search_button = driver.find_element(By.ID, "search")
        search_button.click()

        wait = WebDriverWait(driver, 10)
        table = wait.until(EC.presence_of_element_located((By.ID, "table3")))
        rows = table.find_elements(By.XPATH, "./tbody/tr")

        for row in rows:
            columns = row.find_elements(By.XPATH, "./td")[:8]
            record = [column.text.strip() for column in columns]
            
            if len(record) == 8:
                insert_sql = """
                    INSERT INTO py_mol_input
                    (SerialNumber, CompetentAuthority, AnnouncementDate, DisposalDate, PenaltyFontSize, BusinessUnitName, IllegalLawsAndRegulations, ViolationOfLawsAndRegulations)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """
                cursor.execute(insert_sql, record)
                conn.commit()
                break

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        time.sleep(3)
        driver.quit()
        cursor.close()
        conn.close()

# fetch_data_and_insert_to_py_mol_input()