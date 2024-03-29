<?php

function fetchAndCleanData() {
    // 数据库连接配置
    $host = 'localhost';
    $user = 'root';
    $password = '';
    $db = 'fmras_sql';
    $charset = 'utf8mb4';

    // 创建数据库连接
    $conn = new mysqli($host, $user, $password, $db);

    // 检查连接
    if ($conn->connect_error) {
        die("连接失败: " . $conn->connect_error);
    }

    $conn->set_charset($charset);

    $all_data = array();
    $tables = array('py_prtr_input', 'py_moea_input', 'py_mol_input', 'py_ppstrq_input');

    foreach ($tables as $table) {
        $sql = "SELECT * FROM $table";
        $result = $conn->query($sql);

        $cleaned_result = array();
        if ($result->num_rows > 0) {
            // 输出每行数据
            while($row = $result->fetch_assoc()) {
                if (array_key_exists('AutoNo', $row)) {
                    unset($row['AutoNo']); // 移除 AutoNo 字段
                }
                $cleaned_result[] = $row;
            }
        }
        $all_data[$table] = $cleaned_result; // 存储处理后的每个表的数据
    }

    // 关闭连接
    $conn->close();

    // 将所有数据转换为JSON格式并返回
    return json_encode($all_data, JSON_UNESCAPED_UNICODE);
}
