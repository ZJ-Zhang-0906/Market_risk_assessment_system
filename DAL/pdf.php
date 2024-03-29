<?php
    require_once dirname(__FILE__)."/../SQL/sqlConnect.php";

    class pdf {

        private $conn;
        private $dbName = "pdf";
    
        public function __construct() {
            // Corrected the assignment of $conn
            $this->conn = new sqlConnect("localhost", "root", "", "catchBUG");
        }
        //----------------------------------------------------------------
        //炳申 11/17
        //抓取全部
        public function getAll() 
        {
            $sql = "SELECT * FROM `". $this->dbName."`";

            return $this->conn->executeQuery($sql);
        }
        //----------------------------------------------------------------\
        //炳申 11/17
        //透過pdfName 查詢單表
        public function getOneByPdfName($pdfName) 
        {
            $sql = "SELECT * FROM `". $this->dbName."` WHERE `pdfname` LIKE '".$pdfName."' ";
            
            return $this->conn->executeQuery($sql);
        
        }
        //----------------------------------------------------------------\
        //炳申 11/17
        //查詢單表 條件式查詢
        public function getListByValue($val1 = null, $val2= null,$val3= null)  
        {
            $sql = "SELECT * FROM `". $this->dbName."` WHERE 1 = 1 ";

            if($val1 != null)
            {
                $sql .= " AND '' = '".$val1."' ";
            }
            if($val1 != null)
            {
                $sql .= " AND '' = '".$val1."' ";
            }
            if($val1 != null)
            {
                $sql .= " AND '' = '".$val1."' ";
            }
            
            return $this->conn->executeQuery($sql);
        
        }
        //----------------------------------------------------------------


        
    }
    

?>
  