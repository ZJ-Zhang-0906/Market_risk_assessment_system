<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
    <title>Loading页面</title>
    <link rel="icon" href="assets/font_icon/fonts/ahn4u-wrleu-001.ico" type="image/x-icon">
    <link rel="stylesheet" href="assets/css/loading.css">
</head>

<body>
    <div id="page">
        <div id="container">
            <div id="ring"></div>
            <div id="ring"></div>
            <div id="ring"></div>
            <div id="ring"></div>
            <div id="h3">loading...</div>
        </div>
    </div>

    <br>


    <script>
        document.addEventListener('DOMContentLoaded', function() {
            // 從 localStorage 獲取數據
            const data = localStorage.getItem("formData");
            localStorage.removeItem("formData"); // 清除數據

            fetch('InsertData.php', {
                    method: 'POST',
                    body: data,
                    headers: {
                        "Content-Type": 'application/json',
                    },
                })
                .then(response => response.json())
                .then(data => {
                    if (data.success && data.redirect) {
                        // 根據 InsertData.php 的響應進行跳轉
                        window.location.href = data.redirect;
                    } else {
                        // 處理錯誤情況
                        console.log("錯誤或未提供跳轉地址");
                    }
                })
                .catch(error => {
                    console.error('Error:', error);
                });
        });
    </script>
</body>

</html>