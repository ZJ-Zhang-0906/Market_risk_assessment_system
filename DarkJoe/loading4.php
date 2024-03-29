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
        // JavaScript代码用于在加载后延时跳转
        setTimeout(function() {

            window.location.href = "Risk_end4.php";
        }, 2000); // 5秒后跳转
    </script>
</body>

</html>