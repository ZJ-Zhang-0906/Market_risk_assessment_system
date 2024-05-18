# 安裝
1. 安裝xampp [下載頁面](https://www.apachefriends.org/zh_tw/download.html)
2. 安裝 ChromeDriver 123.0.6312.58 [下載頁面](https://chromedriver.chromium.org/downloads)
3. 建立資料庫
4. 安裝requirements.txt或是npm套件(如果有的話)
------
# 建立資料庫
1. 資料庫名稱 **fmras_sql**
2. 資料表
   - web_input 表
     - AutoNO(int)
     - BusinessAccountingNO(int)
     - CompanyName(text)
     
   - twincn 表
     - AutoNO(int)
     - BusinessAccountingNO(int)
     - CompanyName(text)
     - Lawsuit(text)
   - py_moea_input 表
     - AutoNO(int)
     - BusinessAccountingNO(int)
     - CompanyStatusDesc(text)
     - CompanyName(text)
     - CapitalStockAmount(text)
     - PaidInCapitalAmount(text)
     - ResponsibleName(text)
     - CompanyLocation(text)
   - py_mol_input 表
     - AutoNO (int)
     - SerialNumber(int)
     - CompetentAuthority(text)
     - AnnouncementDate(text)
     - DisposalDate(text)
     - PenaltyFontSize(text)
     - BusinessUnitName(text)
     - IllegalLawsAndRegulations(text)
     - ViolationOfLawsAndRegulations(text)
   - py_ppstrq_input 表
     - AutoNO(int)
     - SerialNumber(int)
     - RegistrationAuthority(text)
     - CaseCategory(text)
     - DebtorName(text)
     - NameOfMortgagee(text)
     - RegistrationNumber(int)
     - CaseStatus(text)
   - py_prtr_input 表
     - AutoNO(int)
     - NumberOfData(int)
------
# 啟動
1. 啟動xampp apache 以及 phpmysql
2. [http://localhost/ProjectNew/DarkJoe/](http://localhost/ProjectNew/DarkJoe/) 或是 [http://127.0.0.1/ProjectNew/DarkJoe/](http://127.0.0.1/ProjectNew/DarkJoe/)
3. 即可使用
------
# 通用專案
## BADREQUIRE.php 跟 BADREQUIRE.css 是一起的

功能:處理客戶端幹了一些不是人幹的事情所指向的錯誤頁面

------

# 風險
### InsertData.php:

功能: 處理由客戶端通過 POST 方法提交的 JSON 數據。
流程:
1. 開始時建立數據庫連接。
2. 讀取和解析客戶端發送的 JSON 數據。
3. 把解析後的數據插入到指定的數據庫表中。
4. 執行一個 Python 腳本，進一步處理或分析數據。
5. 根據 Python 腳本的執行結果，可能重定向到不同的頁面。

### loading.php:

功能: 在用戶提交表單數據後顯示一個加載畫面，並將數據發送到 InsertData.php。
流程:
1. 展示加載動畫。
2. 從 localStorage 獲取數據並發送到 InsertData.php。
3. 根據 InsertData.php 的響應重定向到相應頁面。

## Risk_Assessment-search.php:

功能: 提供一個用戶界面，允許用戶輸入查詢條件。
流程:
1. 顯示一個表單，用戶輸入查詢條件。
2. 在表單提交時，阻止默認提交行為，將數據保存到 localStorage。
3. 將頁面重定向到 loading.php。

### Risk_end.php:

功能: 展示市場風險評估的結果。
流程:
1. 嘗試讀取一個 JSON 文件，該文件包含了處理結果。
2. 如果文件存在，則解析文件並展示數據。
3. 如果文件不存在，顯示錯誤消息。

------
# 財務(研發中)
## Financial.php
1. 使用者輸入頁面
## Financial-Result.php
1. 使用者獲得openai畫面
------
# 炭權
## carbon_rights.php
1. 介紹炭權(須補充更多)

## count_CR.php
1. 計算炭權

------
# 綠能
## GP125.php
1. 介紹綠能(太陽能、小水利、地熱能)

## count_GP.php
1. 計算太陽能的計算機