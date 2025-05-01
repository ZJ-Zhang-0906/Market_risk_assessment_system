<?php
$target_dir = "uploads/";  // 上傳檔案的資料夾
$target_file = $target_dir . basename($_FILES["pdf"]["name"]);

$response = [];

if (isset($_FILES["pdf"])) {
    if (move_uploaded_file($_FILES["pdf"]["tmp_name"], $target_file)) {
        $response["status"] = "success";
        $response["message"] = "檔案已成功上傳： " . $target_file;
    } else {
        $response["status"] = "error";
        $response["message"] = "檔案上傳失敗";
    }
} else {
    $response["status"] = "error";
    $response["message"] = "未選擇檔案";
}

echo json_encode($response);  // 回傳 JSON 結果給前端
?>
