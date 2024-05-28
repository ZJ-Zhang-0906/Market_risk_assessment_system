import os
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pymysql
from selenium.webdriver.chrome.service import Service
# from dotenv import load_dotenv
from fetch import fetch_data_and_insert_to_twincn
from connet_db import connect

# 连接数据库
#===========================================抓所有table資料並轉成json並過濾autono=================================
def fetch_and_clean_data():
    conn, driver = connect()
    cursor = conn.cursor()
    try:
        all_data = {}
        tables = ['py_prtr_input', 'py_moea_input', 'py_mol_input', 'py_ppstrq_input','twincn']

        with conn.cursor(pymysql.cursors.DictCursor) as cursor:
            for table in tables:
                cursor.execute(f"SELECT * FROM {table} ORDER BY AutoNo DESC LIMIT 1")
                result = cursor.fetchall()

                cleaned_result = []
                for row in result:
                    # 移除 'AutoNo' 字段
                    row.pop('AutoNo', None)
                    cleaned_result.append(row)

                all_data[table] = cleaned_result

        # 将所有数据转换为JSON格式
        json_data = json.dumps(all_data, ensure_ascii=False, indent=4)

        # 写入JSON文件
        file_path = r'C:\xampp\htdocs\Market_risk_assessment_system\DarkJoe\data.json'  # 替换为你想要保存的路径
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(json_data)

        return json_data  # 返回文件路径
    finally:
        conn.close()
#============================================================================================
# fetch_and_clean_data()
#==========================================環境部爬汙染======================================== 
def fetch_data_and_insert_to_py_prtr_input():
    conn, driver = connect()
    cursor = conn.cursor()
    try:
        # 編寫SQL查詢，假設資料表名為your_table_name
        sql = "SELECT * FROM web_input ORDER BY AutoNO DESC LIMIT 1"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)

        # 修改這裡來選擇最新的記錄數量
        sql = "SELECT BusinessAccountingNO FROM web_input ORDER BY AutoNO DESC LIMIT 1"

        # 執行查詢
        cursor.execute(sql)

        # 獲取結果
        result = cursor.fetchone()  # 使用fetchone()獲取單條記錄，或使用fetchall()獲取所有結果

        print(result[0])

    except:
        ...

    # 插入資料
    insert_query = """
    INSERT INTO py_prtr_input (NumberOfData)
    VALUES (%s);
    """

    # 打開Google網頁
    driver.get("https://prtr.moenv.gov.tw/deal.html")
    # 找到搜尋框的元素
    search_box = driver.find_element(By.NAME, "UniformNo")
    # 在搜尋框中輸入關鍵字
    search_box.send_keys(result[0])  # 83291953、81020420
    # 查詢公示案件按鈕
    button = driver.find_element(By.CLASS_NAME, "search_submit")
    # 點擊按鈕
    button.click()
    time.sleep(2)
    try:  # 沒有資料
        no_data_div = driver.find_element(By.CLASS_NAME, 'no_data')
        # 在no_data_div内部查找class为'text'的div
        text_element = no_data_div.find_element(By.CLASS_NAME, 'text')
        # 获取元素中的文本
        text = text_element.text
        print(text)
    except:  # 有資料
        have_data = driver.find_element(By.CLASS_NAME, 'result_number')
        text = have_data.text
        print(text)

    try:
        cursor.execute(insert_query, (text,))
        conn.commit()
    except pymysql.MySQLError as e:
        print("Error in SQL execution: ", e)
        conn.rollback()

    # 等待一些時間，以便查看搜尋結果
    time.sleep(1)

    driver.quit()

#=========================================================================================


fetch_and_clean_data()