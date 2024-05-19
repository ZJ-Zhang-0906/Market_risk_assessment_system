<?php

$host = 'localhost';
$dbuser = 'root';
$dbpassword = '';
$dbname = 'fmras_sql';

$response = [
    "success" => false,
    "message" => "",
    "redirect" => []
];

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    header('Content-Type: application/json'); // 确保在输出之前设置

    $conn = new mysqli($host, $dbuser, $dbpassword, $dbname);

    if ($conn->connect_error) {
        $response["message"] = "连接失败: " . $conn->connect_error;
        echo json_encode($response);
        exit; // 确保在连接失败时终止脚本
    }

    $json_data = file_get_contents('php://input');
    $requestData = json_decode($json_data, true);

    if (!$requestData) {
        $response["message"] = "无效的JSON数据";
        echo json_encode($response);
        exit; // 处理无效JSON
    }

    $CompanyName = $requestData['CompanyName'];
    $UniformNumbers = $requestData['UniformNumbers'];

    $stmt = $conn->prepare("INSERT INTO web_input (CompanyName, BusinessAccountingNO) VALUES (?, ?)");
    $stmt->bind_param("ss", $CompanyName, $UniformNumbers);

    if ($stmt->execute()) {
        $response["success"] = true;
        $response["message"] = "Insert success";
    } else {
        $response["message"] = "Insert failure";
    }
    $stmt->close();
    $conn->close();

    // 删除旧的 JSON 文件（如果存在）
    $jsonFilePath = 'C:/xampp/htdocs/Market_risk_assessment_system/DarkJoe/data.json';//替换为你想要保存的路径
    if (file_exists($jsonFilePath)) {
        unlink($jsonFilePath); // 删除文件
    }


    // 执行 Python 脚本
    $scriptPath = 'C:/xampp/htdocs/Market_risk_assessment_system/DarkJoe/pyy/main.py';//替换为你想要保存的路径
    $pythonPath = 'C:/Users/ZJ/AppData/Local/Programs/Python/Python311/python.exe';//替换为你想要保存的路径

    $command = escapeshellcmd("$pythonPath $scriptPath");
    $output = shell_exec($command);


    // 检查 Python 脚本生成的新 JSON 文件
    if (file_exists($jsonFilePath)) {
        $jsonContent = file_get_contents($jsonFilePath);
        $response["data"] = json_decode($jsonContent, true);
        $response["redirect"] = "Risk_end.php"; // 设置重定向目标
    } else {
        $response["message"] = "Python 脚本未生成预期的输出文件";
        $response["redirect"] = "Risk_Assessment-search.php?error=" . urlencode($response["message"]);
    }
    
    echo json_encode($response); // 发送 JSON 响应
}