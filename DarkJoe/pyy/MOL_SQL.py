from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pymysql
from selenium.webdriver.chrome.service import Service
from connet_db import connect
# 環境不 汙染
#-----------------------------------齊齊-2024-01-19-資料庫連接------------------------------------------------------------------------------------
    conn, driver = connect()
    cursor = conn.cursor()
#-----------------------------------------------------------------------------------------------
# 索引資料表資料
try:
    # 編寫SQL查詢，假設資料表名為your_table_name
    sql = "SELECT CompanyName FROM web_input ORDER BY AutoNO DESC LIMIT 1"
    cursor.execute(sql)
    result = cursor.fetchone()  # 獲取單條記錄
    if result:
        company_name = result[0]  # 獲取 'CompanyName' 的值
        print(company_name)
    else:
        print("No company name found.")
        company_name = ""  # 如果沒有找到結果，設定一個默認值
except:
    ...



# SQL 插入语句
insert_sql = """
    INSERT INTO py_mol_input
    (SerialNumber, CompetentAuthority, AnnouncementDate, DisposalDate, PenaltyFontSize, BusinessUnitName, IllegalLawsAndRegulations, ViolationOfLawsAndRegulations)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
"""

# 设置 Chrome 驱动
driver = webdriver.Chrome(service = service)
driver.get("https://announcement.mol.gov.tw/")
# 找到搜尋框的元素
search_box = driver.find_element(By.NAME, "UNITNAME")
# 在搜尋框中輸入關鍵字
search_box.send_keys(company_name)  # 聯發科技

button = driver.find_elements(By.ID, "search")
# 點擊按鈕
button[0].click()

# 等待页面元素加载完毕
wait = WebDriverWait(driver, 10)
table = wait.until(EC.presence_of_element_located((By.ID, "table3")))

rows = table.find_elements(By.XPATH, "./tbody/tr")

# 处理表格中的数据
for row in rows:
    columns = row.find_elements(By.XPATH, "./td")
    columns = columns[:8]  # 只保留前8个元素
    record = [column.text.strip() for column in columns]
    print(record)

    if len(record) == 1 and record[0] == "查無資料":
        # 如果只有一个元素且内容为"查無資料"，则创建一个全是"查無資料"的记录
        record = ["查無資料"] * 8

    if len(record) == 8:
        # 检查数据是否已存在
        # check_sql = "SELECT * FROM py_mol_input WHERE SerialNumber = %s"
        # cursor.execute(check_sql, (record[0],))
        result = cursor.fetchone()

        if not result:
            try:
                cursor.execute(insert_sql, record)
                conn.commit()
                break  # 插入后退出循环
            except pymysql.MySQLError as e:
                print("Error in SQL execution: ", e)
                conn.rollback()
import time  # 导入 time 模块

# 等待10秒
time.sleep(3)
# 关闭浏览器驱动和数据库连接

driver.quit()

cursor.close()
conn.close()