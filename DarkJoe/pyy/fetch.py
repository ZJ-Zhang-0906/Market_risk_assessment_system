import pymysql
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from connet_db import connect
#==================================台灣公司網爬訴訟=================================================
def fetch_data_and_insert_to_twincn():
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

            # 使用 Selenium 访问特定页面
            driver.get(f"https://www.twincn.com/item.aspx?no={business_accounting_no}")
            time.sleep(3)  # 等待页面加载

            # 提取页面上的公司名称和法律信息
            h1_element = driver.find_element(By.CSS_SELECTOR, 'h1')
            company_name = h1_element.text  # 提取公司名称
            lawsuit_elements = driver.find_elements(By.CSS_SELECTOR, '#page4 .table-responsive tbody tr td')
            lawsuit_text = ' '.join([el.text for el in lawsuit_elements])  # 合并法律信息文本

            # 构建数据库插入语句
            insert_sql = """
                INSERT INTO twincn (BusinessAccountingNO, CompanyName, Lawsuit)
                VALUES (%s, %s, %s);
            """
            # 执行插入操作
            cursor.execute(insert_sql, (business_accounting_no, company_name, lawsuit_text))
            conn.commit()
            print("Data inserted successfully")

    except Exception as e:
        print(f"An error occurred: {e}")
        conn.rollback()  # 回滚在异常时的所有更改
    finally:
        # 关闭浏览器和数据库连接
        driver.quit()
        cursor.close()
        conn.close()

# 调用函数
# fetch_data_and_insert_to_db()
#====================================================================================================