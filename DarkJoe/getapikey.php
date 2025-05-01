<?php
// 載入 .env 檔案
require_once __DIR__ . '/../vendor/autoload.php';

use Dotenv\Dotenv;

// 啟用錯誤顯示
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

// 載入 .env 檔案
$dotenv = Dotenv::createImmutable(__DIR__.'/../');
$dotenv->load();

// 檢查 OPENAI_API_KEY 是否存在
if (!isset($_ENV['OPENAI_API_KEY']) || empty($_ENV['OPENAI_API_KEY'])) {
    http_response_code(500); // 返回 500 內部伺服器錯誤
    echo json_encode(['error' => 'API Key not found in .env file']);
    exit;
}

// 獲取 API 金鑰
$apiKey = $_ENV['OPENAI_API_KEY'];

// 返回 API 金鑰作為 JSON 格式
echo json_encode(['api_key' => $apiKey]);
?>
