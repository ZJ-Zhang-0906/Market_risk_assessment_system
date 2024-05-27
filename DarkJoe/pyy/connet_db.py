
import pymysql
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

#======================================連線db、設置chromedriver位址===========================
def connect():
    # 设置 Chrome 驱动器路径
    driver_path = r'C:\xampp\htdocs\Market_risk_assessment_system\DarkJoe\pyy\chromedriver-win64\chromedriver.exe'
    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service)
    
    # 数据库连接配置
    host = 'localhost'
    user = 'root'
    password = ''
    db = 'fmras_sql'
    conn = pymysql.connect(host=host, user=user, password=password, database=db, charset='utf8mb4')
    
    # 返回数据库连接和WebDriver对象
    return conn, driver

#=======================================================================================================

# connect()