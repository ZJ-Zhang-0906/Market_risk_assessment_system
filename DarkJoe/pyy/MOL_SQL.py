from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pymysql
from selenium.webdriver.chrome.service import Service
from connet_db import connect
import time
from datetime import datetime, timedelta

#----------------------------------勞動部 勞基法 三年內------------------------------------------------------------------------------------



def fetch_data_and_insert_to_py_mol_input():
    conn, driver = connect()  # 使用connect函数来获取连接和驱动器
    try:
        cursor = conn.cursor()

        # 获取最新的公司名称
        sql = "SELECT CompanyName FROM web_input ORDER BY AutoNO DESC LIMIT 1"
        cursor.execute(sql)
        result = cursor.fetchone()
        if result:
            # company_name = '中國信託'  測試用
            
            company_name = result[0]
        else:
            print("No company name found.")
            return

        # 计算民国日期
        today = datetime.now()
        last_year = today - timedelta(days=365)
        today_tw = f"{today.year - 1911}{today.month:02}{today.day:02}"
        last_year_tw = f"{last_year.year -1911}{last_year.month:02}{last_year.day:02}"

        driver.get("https://announcement.mol.gov.tw/")

        # 设置日期
        driver.find_element(By.NAME, "DOCstartDate").send_keys(last_year_tw)
        driver.find_element(By.NAME, "DOCEndDate").send_keys(today_tw)

        search_box = driver.find_element(By.NAME, "UNITNAME")
        search_box.send_keys(company_name)
        search_button = driver.find_element(By.ID, "search")
        search_button.click()

        wait = WebDriverWait(driver, 5)
        table = wait.until(EC.presence_of_element_located((By.ID, "table3")))
        rows = table.find_elements(By.XPATH, "./tbody/tr")

        # 检查是否有数据
        if rows and '查無資料' not in rows[0].text:
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
        else:
            print("No data found, inserting 0 into database.")
            insert_sql = """
                INSERT INTO py_mol_input
                (SerialNumber, CompetentAuthority, AnnouncementDate, DisposalDate, PenaltyFontSize, BusinessUnitName, IllegalLawsAndRegulations, ViolationOfLawsAndRegulations)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            # 使用占位符0插入資料
            cursor.execute(insert_sql, (0, 0, 0, 0, 0, 0, 0, 0))
            conn.commit()

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        time.sleep(3)
        driver.quit()
        cursor.close()
        conn.close()

fetch_data_and_insert_to_py_mol_input()
#-----------------------------------------------------------------------------------------------