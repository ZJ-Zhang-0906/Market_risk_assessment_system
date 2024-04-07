<?php

// 更正變量名稱
$host = 'localhost';
$dbuser = 'root';
$dbpassword = '';
$dbname = 'fmras_sql';

$response = [
    "success" => false,
    "message" => "",
    "pythonOutput" => [] // 明确初始化为一个空数组
];
// 檢查表單是否已提交
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // 建立連接
    $conn = new mysqli($host, $dbuser, $dbpassword, $dbname);

    // 檢查連接
    if ($conn->connect_error) {
        die("連接失敗: " . $conn->connect_error);
    }

    $json_data = file_get_contents('php://input');
    $requestData = json_decode($json_data, true);

    $CompanyName = $requestData['CompanyName'];
    $UniformNumbers = $requestData['UniformNumbers'];

    // 預備和綁定
    $stmt = $conn->prepare("INSERT INTO web_input (CompanyName, BusinessAccountingNO) VALUES (?, ?)");
    $stmt->bind_param("ss", $CompanyName, $UniformNumbers);
   
    if ($stmt->execute()) {
        $response["success"] = true;
        $response["message"] = "Insert success";
    } else {
        $response["success"] = false;
        $response["message"] = "Insert failure";
    }
    $stmt->close();
    $conn->close();

    // echo json_encode($data);

    // 脚本路径，相对于当前PHP脚本的位置
    $scriptPath = 'C:/xampp/htdocs/ProjectNew/DarkJoe/pyy/main.py';

    $pythonPath = 'C:/Users/ZJ/AppData/Local/Programs/Python/Python311/python.exe'; // 或根据您的环境配置适当修改

    $command = escapeshellcmd("$pythonPath $scriptPath");
    // 执行Python脚本并捕获输出
    $output = shell_exec($command);
    // 将输出添加到响应数组
    $response["pythonOutput"] = $output;

    // 发送JSON响应
    header('Content-Type: application/json');
    echo json_encode($response);
}
