<?php
   require_once (dirname(__FILE__) ."/DAL/StoreNameDAL.php");
    
    $aDAL1 = new StoreNameDAL();

    $aInfo1 = $aDAL1->getAll();

    echo print_r($aInfo1);


?>