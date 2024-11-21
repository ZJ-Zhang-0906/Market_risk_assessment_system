<!DOCTYPE html>
<html lang="ZH_TW">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="assets/css/BADREQUIRE.css">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <title>錯誤</title>
</head>

<body>
    <div class="row justify-content-center mt-2  ">
        <div class="col-auto">
            <button type="button" class="btn btn-primary">
                <a class="linkFontColor" href="index.php">回首頁</a>
            </button>
        </div>
    </div>
    <div class="badrequire " id="badrequire">
        <!-- <img src="assets/images/images.jpg" alt="海綿寶包"> -->
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
    <script>
        // 创建包含图片 URL 的对象
        let person = {
            1: "./assets/images/images.jpg",
            2: "./assets/images/pp.jpeg",
            3: "./assets/images/pp2.jpg"
        };

        // 生成一个 0 到 2 之间的随机整数
        let randomInt = Math.floor(Math.random() * 3) + 1;

        // 根据随机整数获取对应的图片 URL
        let randomImageSrc = person[randomInt];

        // 创建 img 元素并设置 src 属性
        let imgElement = document.createElement("img");
        imgElement.src = randomImageSrc;

        // 将 img 元素插入到指定的 div 中
        let badrequireDiv = document.getElementById("badrequire");
        badrequireDiv.appendChild(imgElement);
    </script>
</body>

</html>