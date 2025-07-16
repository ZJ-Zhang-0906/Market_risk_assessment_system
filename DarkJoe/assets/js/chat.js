 async function getApiKey() {
    try {
        const response = await fetch('../DarkJoe/getapikey.php'); // 請求 PHP 文件
        console.log(response);
        // 確保回應是 JSON 格式
        const data = await response.json(); // 解析 JSON 資料
        // 檢查 data 是否有 api_key
        if (!data.api_key) {
            throw new Error('API key not found in the response');
        }
        const apiKey = data.api_key; // 提取 API 金鑰
        // 使用這個金鑰來進行其他 API 呼叫
    } catch (error) {
        console.error('Error fetching API key:', error); // 顯示錯誤訊息
    }
}

// 上傳檔案的 JavaScript 函數
function uploadFile() {
    const fileInput = document.getElementById('pdf');
    const formData = new FormData();
    formData.append('pdf', fileInput.files[0]);  // 將檔案添加到 FormData
    console.log(formData);  // 修正拼寫錯誤
    
    const statusDiv = document.getElementById('upload-status');
    statusDiv.style.display = 'none';  // 重置顯示

    // 發送檔案上傳請求
    fetch('upload.php', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())  // 修正回傳值問題
    .then(data => {
        console.log(data);
        if (data.status === 'success') {
            statusDiv.innerHTML = '檔案上傳成功！';
            statusDiv.style.display = 'block';
        } else {
            statusDiv.innerHTML = '檔案上傳失敗。請重試。';
            statusDiv.style.display = 'block';
        }
    })
    .catch(error => {
        console.error('Error uploading file:', error);
        statusDiv.innerHTML = '檔案上傳過程中出現錯誤。';
        statusDiv.style.display = 'block';
    });

}