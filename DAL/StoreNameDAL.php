<?php

    require_once (dirname(__FILE__) ."/../SQL/sqlConnect.php");
   
    class StoreNameDAL {

        private $conn;
        private $dbName = "store_name";
    
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
      

        
    }


?>
  