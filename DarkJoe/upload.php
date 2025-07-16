<?php
header('Content-Type: application/json');

// ✅ log function
function write_log($message) {
    $log_dir = __DIR__ . '/logs';
    if (!is_dir($log_dir)) mkdir($log_dir, 0755, true);
    $log_file = $log_dir . '/upload_log.txt';
    $timestamp = date('[Y-m-d H:i:s]');
    file_put_contents($log_file, "$timestamp $message\n", FILE_APPEND);
}

try {
    if (!isset($_FILES['pdf']) || $_FILES['pdf']['error'] !== UPLOAD_ERR_OK) {
        $error_code = isset($_FILES['pdf']) ? $_FILES['pdf']['error'] : 'no_file';
        write_log("檔案上傳失敗，錯誤碼: $error_code");
        echo json_encode(['status' => 'error', 'message' => '檔案上傳失敗，錯誤碼: ' . $error_code]);
        exit;
    }

    $upload_dir = 'uploads/';
    if (!is_dir($upload_dir) && !mkdir($upload_dir, 0755, true)) {
        write_log("無法創建上傳目錄：$upload_dir");
        echo json_encode(['status' => 'error', 'message' => '無法創建上傳目錄']);
        exit;
    }

    $filename = date('YmdHis') . '_' . $_FILES['pdf']['name'];
    $filepath = $upload_dir . $filename;

    if (!move_uploaded_file($_FILES['pdf']['tmp_name'], $filepath)) {
        write_log("檔案移動失敗：$filepath");
        echo json_encode(['status' => 'error', 'message' => '檔案移動失敗，請檢查目錄權限']);
        exit;
    }

    write_log("檔案成功上傳至：$filepath");

    // ✅ 指定 Python 路徑（根據你 InsertData 的範例）
    $python = 'C:/Users/ZJ/AppData/Local/Programs/Python/Python311/python.exe';//執行主要py檔案 替换为你想要保存的路径
    $escaped_path = escapeshellarg($filepath);
    $cmd = "chcp 65001 >nul & $python pyy/chat.py upload $escaped_path 2>&1";//執行主要py檔案 替换为你想要保存的路径
    write_log("執行命令：$cmd");

    $output = shell_exec($cmd);
    write_log("Python 回傳：$output");

    if (!$output || strpos($output, '|') === false) {
        write_log("向量建檔失敗。輸出為：$output");
        echo json_encode(['status' => 'error', 'message' => 'AI 向量建檔失敗或無法解析回傳格式']);
        exit;
    }

    list($file_id, $vector_id) = explode('|', trim($output));
    write_log("建檔成功：file_id=$file_id, vector_store_id=$vector_id");

    echo json_encode([
        'status' => 'uploaded',
        'message' => '檔案與向量庫已建立成功',
        'file_id' => $file_id,
        'vector_id' => $vector_id
    ]);

} catch (Exception $e) {
    $msg = '伺服器錯誤: ' . $e->getMessage();
    write_log($msg);
    echo json_encode(['status' => 'error', 'message' => $msg]);
}
