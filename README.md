

##InsertData.php:

功能: 處理由客戶端通過 POST 方法提交的 JSON 數據。
流程:
開始時建立數據庫連接。
讀取和解析客戶端發送的 JSON 數據。
把解析後的數據插入到指定的數據庫表中。
執行一個 Python 腳本，進一步處理或分析數據。
根據 Python 腳本的執行結果，可能重定向到不同的頁面。
loading.php:

功能: 在用戶提交表單數據後顯示一個加載畫面，並將數據發送到 InsertData.php。
流程:
展示加載動畫。
從 localStorage 獲取數據並發送到 InsertData.php。
根據 InsertData.php 的響應重定向到相應頁面。

Risk_Assessment-search.php:

功能: 提供一個用戶界面，允許用戶輸入查詢條件。
流程:
顯示一個表單，用戶輸入查詢條件。
在表單提交時，阻止默認提交行為，將數據保存到 localStorage。
將頁面重定向到 loading.php。

Risk_end.php:
功能: 展示市場風險評估的結果。
流程:
嘗試讀取一個 JSON 文件，該文件包含了處理結果。
如果文件存在，則解析文件並展示數據。
如果文件不存在，顯示錯誤消息。