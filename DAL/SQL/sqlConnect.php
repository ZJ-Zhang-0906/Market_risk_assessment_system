<?php
    class sqlConnect 
    {
        private $servername;
        private $username;
        private $password;
        private $dbname;
        public $conn;

        public function __construct($servername, $username, $password, $dbname) {
            $this->servername = $servername;
            $this->username = $username;
            $this->password = $password;
            $this->dbname = $dbname;

            // 嘗試連接到數據庫
            $this->conn = new mysqli($this->servername, $this->username, $this->password, $this->dbname);

            // 檢查連接
            if ($this->conn->connect_error) {
                die("連接失敗: " . $this->conn->connect_error);
            }
            echo "連接成功";
        }

        // 這裡你可以添加更多方法，比如執行查詢等

        // 當物件不再使用時關閉數據庫連接
        public function __destruct() 
        {
            $this->conn->close();
        }

        public function executeQuery($sql) 
        {
            $result = $this->conn->query($sql);
        

            if ($result === false) {
                // 處理錯誤情況
                return [];
            }
        
            $rows = [];
            while ($row = $result->fetch_assoc()) {
                $rows[] = $row;
            }
            return $rows;
        }
        
    }

?>
