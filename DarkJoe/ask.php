<?php
header('Content-Type: application/json');

// ✅ 紀錄 log
function write_log($message) {
    $log_dir = __DIR__ . '/logs';
    if (!is_dir($log_dir)) mkdir($log_dir, 0755, true);
    $log_file = $log_dir . '/ask_log.txt';
    $timestamp = date('[Y-m-d H:i:s]');
    file_put_contents($log_file, "$timestamp $message\n", FILE_APPEND);
}

if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['question']) && isset($_POST['vector_id'])) {
    $question = $_POST['question'];
    $vector_id = $_POST['vector_id'];

    $python = 'C:/Users/ZJ/AppData/Local/Programs/Python/Python311/python.exe';//執行主要py檔案 替换为你想要保存的路径
    $escaped_question = escapeshellarg($question);
    $escaped_vector = escapeshellarg($vector_id);

    $cmd = "chcp 65001 >nul & $python pyy/chat.py ask $escaped_vector $escaped_question 2>&1";//執行主要py檔案 替换为你想要保存的路径
    write_log("執行命令：$cmd");

    $output = shell_exec($cmd);
    write_log("Python 回傳：$output");

    if (trim($output) !== '') {
        echo json_encode(["status" => "answered", "reply" => $output]);
    } else {
        write_log("查詢失敗或 Assistant 沒回應。");
        echo json_encode(["status" => "error", "message" => "AI 查詢失敗或 Assistant 無回應"]);
    }
} else {
    write_log("接收參數錯誤：" . json_encode($_POST));
    echo json_encode(["status" => "error", "message" => "缺少必要參數"]);
}
?>
