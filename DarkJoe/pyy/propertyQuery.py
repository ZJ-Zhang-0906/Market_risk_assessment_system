import pymysql
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from connet_db import connect

def fetch_data_and_insert_to_py_ppstrq_input():
    # 使用 connect 函数获取数据库连接和WebDriver对象
    conn, driver = connect()
    cursor = conn.cursor()

    try:
        # 从数据库获取最新的 BusinessAccountingNO
        sql = "SELECT BusinessAccountingNO FROM web_input ORDER BY AutoNO DESC LIMIT 1"
        cursor.execute(sql)
        result = cursor.fetchone()
        if result:
            business_accounting_no = result[0]
            print(f"BusinessAccountingNO: {business_accounting_no}")

            # 使用 Selenium 打开页面并搜索
            driver.get("https://ppstrq.nat.gov.tw/pps/pubQuery/PropertyQuery/propertyQuery.do")
            search_box = driver.find_element(By.NAME, "queryDebtorNo")
            search_box.send_keys(business_accounting_no)
            button = driver.find_element(By.CLASS_NAME, "myButtonLong")
            button.click()
            time.sleep(3)

            try:
                # 尝试找到无数据的消息
                no_data_element = driver.find_element(By.CSS_SELECTOR, '#message span.label.label-danger')
                print(no_data_element.text)  # 查无符合案件!!
                if no_data_element.text == "查無符合案件!!":
                    # 如果没有数据，执行一个插入全为0的数据的操作
                    data_to_insert = ("0", "0", "0", "0", "0", "0", "0")
                    insert_sql = """
                        INSERT INTO py_ppstrq_input
                        (SerialNumber, RegistrationAuthority, CaseCategory, DebtorName, NameOfMortgagee, RegistrationNumber, CaseStatus)
                        VALUES (%s, %s, %s, %s, %s, %s, %s)
                    """
                    cursor.execute(insert_sql, data_to_insert)
                    conn.commit()
            except:
                # 如果有数据，提取表格内容
                table_xpath = '//tr[@class="td_odd"]'
                table_row = driver.find_element(By.XPATH, table_xpath)
                columns = table_row.find_elements(By.TAG_NAME, 'td')
                table_data = [column.text for column in columns]
                print(table_data)  # 打印表格数据
                if len(table_data) == 7:  # 确保数据列的数量正确
                    # 执行插入操作
                    insert_sql = """
                        INSERT INTO py_ppstrq_input
                        (SerialNumber, RegistrationAuthority, CaseCategory, DebtorName, NameOfMortgagee, RegistrationNumber, CaseStatus)
                        VALUES (%s, %s, %s, %s, %s, %s, %s)
                    """
                    cursor.execute(insert_sql, tuple(table_data))
                    conn.commit()

    except Exception as e:
        print(f"发生错误: {e}")
        conn.rollback()
    finally:
        # 关闭浏览器和数据库连接
        driver.quit()
        cursor.close()
        conn.close()

# 使用这个函数
# fetch_data_and_insert_to_py_ppstrq_input()
