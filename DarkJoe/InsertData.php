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

    $logFilePath = 'C:/xampp/htdocs/Market_risk_assessment_system/DarkJoe/python_script.log';

    // 初始化日志文件
    file_put_contents($logFilePath, "Script started\n", FILE_APPEND);

    try {
        $conn = new mysqli($host, $dbuser, $dbpassword, $dbname);

        if ($conn->connect_error) {
            $response["message"] = "连接失败: " . $conn->connect_error;
            file_put_contents($logFilePath, "数据库连接失败: " . $conn->connect_error . "\n", FILE_APPEND);
            echo json_encode($response);
            exit; // 确保在连接失败时终止脚本
        }

        $json_data = file_get_contents('php://input');
        $requestData = json_decode($json_data, true);

        if (!$requestData) {
            $response["message"] = "无效的JSON数据";
            file_put_contents($logFilePath, "无效的JSON数据\n", FILE_APPEND);
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
            file_put_contents($logFilePath, "数据插入成功\n", FILE_APPEND);
        } else {
            $response["message"] = "Insert failure";
            file_put_contents($logFilePath, "数据插入失败\n", FILE_APPEND);
        }
        $stmt->close();
        $conn->close();

        // 删除旧的 JSON 文件（如果存在）
        $jsonFilePath1 = 'C:/xampp/htdocs/Market_risk_assessment_system/DarkJoe/data.json';
        $jsonFilePath2 = 'C:/xampp/htdocs/Market_risk_assessment_system/DarkJoe/respon.json';

        if (file_exists($jsonFilePath1)) {
            unlink($jsonFilePath1);
            file_put_contents($logFilePath, "旧的data.json文件已删除\n", FILE_APPEND);
        }
        if (file_exists($jsonFilePath2)) {
            unlink($jsonFilePath2);
            file_put_contents($logFilePath, "旧的respon.json文件已删除\n", FILE_APPEND);
        }

        // 执行 Python 脚本
        $scriptPath = 'C:/xampp/htdocs/Market_risk_assessment_system/DarkJoe/pyy/main.py';
        $pythonPath = 'C:/Users/ZJ/AppData/Local/Programs/Python/Python311/python.exe';

        $command = "$pythonPath $scriptPath 2>&1";
        file_put_contents($logFilePath, "执行命令: $command\n", FILE_APPEND);

        // 运行命令并捕获输出
        $output = shell_exec($command);

        // 将输出写入日志文件
        file_put_contents($logFilePath, "命令输出: $output\n", FILE_APPEND);

        if ($output === null) {
            $response["message"] = "执行Python脚本时发生错误";
            file_put_contents($logFilePath, "执行Python脚本时发生错误\n", FILE_APPEND);
        } else {
            $response["message"] = "Python脚本输出已写入日志文件";
            file_put_contents($logFilePath, "Python脚本输出已写入日志文件\n", FILE_APPEND);
        }

        // 检查 Python 脚本生成的新 JSON 文件
        if (file_exists($jsonFilePath1) && file_exists($jsonFilePath2)) {
            $jsonContent1 = file_get_contents($jsonFilePath1);
            $jsonContent2 = file_get_contents($jsonFilePath2);
            $response["data1"] = json_decode($jsonContent1, true);
            $response["data2"] = json_decode($jsonContent2, true);
            $response["redirect"] = "Risk_end.php"; // 设置重定向目标
            file_put_contents($logFilePath, "新的JSON文件已生成\n", FILE_APPEND);
        } else {
            $response["message"] = "Python 脚本未生成预期的输出文件";
            $response["redirect"] = "Risk_Assessment-search.php?error=" . urlencode($response["message"]);
            file_put_contents($logFilePath, "Python脚本未生成预期的输出文件\n", FILE_APPEND);
        }
    } catch (Exception $e) {
        $response["message"] = "脚本执行过程中发生异常: " . $e->getMessage();
        file_put_contents($logFilePath, "脚本执行过程中发生异常: " . $e->getMessage() . "\n", FILE_APPEND);
    }

    echo json_encode($response); // 发送 JSON 响应
}
