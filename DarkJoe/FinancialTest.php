<?php
$terms = [
    "銀行借款對淨值比率" => "請幫我計算出銀行借款對淨值比率，他的公式是:銀行借款/淨利,盡量簡短回覆",
    "權益總額" => "請幫我計算出權益總額，他的公式是:全部資產減全部負債後的凈資產,盡量簡短回覆",
    "長期銀行借款對淨值比率" => "請幫我計算出長期銀行借款對淨值比率，他的公式是:長期銀行借款/淨利,盡量簡短回覆",
    "槓桿比率" => "請幫我計算出槓桿比率，他的公式是:負債總額/淨利,盡量簡短回覆",
    "流動比率" => "請幫我計算出流動比率，他的公式是:(流動資產總計/流動負債總計)*100,盡量簡短回覆",
    "速動比率" => "請幫我計算出速動比率，他的公式是:(速動資產總計/流動負債總計)*100,盡量簡短回覆",
    "存貨週轉率" => "請幫我計算出存貨週轉率，他的公式是:營業成本/存貨,盡量簡短回覆",
    "營運資金週轉率" => "請幫我計算出營運資金週轉率，他的公式是:營業收入/營運資金淨額,盡量簡短回覆",
    "純益率(稅後)" => "請幫我計算出純益率(稅後)，他的公式是:稅後損益/營業收入,盡量簡短回覆",
    "淨值報酬率(稅後)" => "請幫我計算出淨值報酬率(稅後)，他的公式是:稅後損益/淨利,盡量簡短回覆",
    "營業活動之淨現金流量對短期銀行借款比率" => "請幫我計算出營業活動之淨現金流量對短期銀行借款比率，他的公式是:營業活動之淨現金流量/短期銀行借款,盡量簡短回覆",
    "資本支出對固定資產淨額比率" => "請幫我計算出資本支出對固定資產淨額比率，他的公式是:資本支出/固定資產淨額,盡量簡短回覆",
    "現金流量比率" => "請幫我計算出現金流量比率，他的公式是:營業活動之淨現金流量/流動負債總計,盡量簡短回覆",
    "債本比(信保之負債比率)" => "請幫我計算出債本比(信保之負債比率)，他的公式是:(負債/淨利)*100,盡量簡短回覆",
    "固定長期適合率" => "請幫我計算出固定長期適合率，他的公式是:((固定資產+長投)/(淨利+長負))*100,盡量簡短回覆",
    "存货週轉天數" => "請幫我計算出存货週轉天數，他的公式是:365/(銷貨成本/平均存貨),盡量簡短回覆",
    "應收款週轉天數" => "請幫我計算出應收款週轉天數，他的公式是:365/(銷貨收入淨額/平均應收帳款),盡量簡短回覆",
    "應付款週轉天數" => "請幫我計算出應付款週轉天數，他的公式是:365/(銷貨成本/平均應付款),盡量簡短回覆",
    "現金循環天數" => "請幫我計算出現金循環天數，他的公式是:(存货週轉天數)+(應收款週轉天數)-(應付款週轉天數),盡量簡短回覆",
    "利息保障倍數" => "請幫我計算出利息保障倍數，他的公式是:(稅前損益+利息費用+折舊費用+攤銷費用)/利息費用,盡量簡短回覆",
    "銷貨成長率" => "請幫我計算出銷貨成長率，他的公式是:(本期銷貨/上期銷貨-1)*100,盡量簡短回覆",
];

?>

<!DOCTYPE html>
<html class="no-js " lang="ZH_TW">

<head>
    <title>預測</title>
    <link rel="icon" href="assets/font_icon/fonts/ahn4u-wrleu-001.ico" type="image/x-icon">

    <!-- meta -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">

    <!-- stylesheets -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-F3w7mX95PdgyTmZZMECAngseQB83DfGTowi0iMjiWaeVhAn4FJkqJByhZMI3AhiU" crossorigin="anonymous">
    <link rel="stylesheet" href="assets/css/bootstrap.min.css">
    <link rel="stylesheet" href="assets/font_icon/css/pe-icon-7-stroke.css">
    <link rel="stylesheet" href="assets/font_icon/css/helper.css">
    <link rel="stylesheet" href="assets/css/Financial.css">
    <link rel="stylesheet" href="assets/css/owl.carousel.css">
    <link rel="stylesheet" href="assets/css/owl.theme.css">
    <link rel="stylesheet" href="assets/css/animate.css">
    <link rel="stylesheet" href="assets/css/style.css">
    <link rel="stylesheet" href="assets/css/nav.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
</head>

<body id="body">
    <!-- Navigation area -->
    <section id="navigation">
        <div class="container">
            <div class="row">
                <div class="col-xs-2" style=" font-size: x-large; display: flex; ">
                    <a href="index.php">
                        <i><span class=" pe-7s-home in "></span>
                        </i>
                    </a>
                </div>
                <div class="col-xs-8">
                    <div class="content"><a data-scroll href="#body" class="logo-text" style="font-family:sans-serif; font-size: 30px;text-align: center; display: flex; flex-direction: initial;align-items: baseline; justify-content: center;">市場風險<br>評估系統</a>
                    </div>
                </div>
                <div class="col-xs-2">
                    <div class="nav">
                        <a href="#" data-placement="bottom" title="Menu" class="menu" data-toggle="dropdown"><i class="pe-7s-menu"></i></a>
                        <a href="#"></a>
                        <div class="dropdown-menu" style="background: #ffffff;">
                            <div class="arrow-up"></div>
                            <ul>
                                <a href="index.php">
                                    <li class="menu-item"><i data-scroll>相關服務</i><span class="menu-effect pe-7s-search" style="padding-left :85px;;font-size: 27px;"></span>
                                    </li>
                                </a>
                                <a href="index.php">
                                    <li class="menu-item"><i data-scroll>相關網站連結</i><span class="menu-effect pe-7s-link" style="font-size: 27px; padding-left: 48.5px;"></span>
                                    </li>
                                </a>
                                <a href="Risk_Assessment-search.php">
                                    <li class="menu-item"><i data-scroll>風險評估</i><span class="menu-effect pe-7s-search" style="font-size: 27px; padding-left: 85px;"></span>
                                    </li>
                                </a>
                                <a href="Financial.php">
                                    <li class="menu-item"><i data-scroll>財務分析</i><span class="menu-effect pe-7s-news-paper" style="font-size: 27px; padding-left: 85px;"></span>
                                    </li>
                                </a>
                                <a href="Contact_Us.php">
                                    <li class="menu-item"><i data-scroll>與我們聯繫</i><span class="menu-effect pe-7s-call pe-dj pe-va" style="font-size: 27px; padding-left: 67px;"></span>
                                    </li>
                                </a>
                                <a href="carbon_rights.php">
                                    <li class="menu-item"><i data-scroll>碳權是什麼</i><span class="menu-effect fa fa-leaf pe-dj pe-va" style="font-size: 27px; padding-left: 64px;"></span>
                                    </li>
                                </a>
                                <a href="GP125.php">
                                    <li class="menu-item"><i data-scroll>綠能是什麼</i><span class="menu-effect  pe-7s-light pe-dj pe-va" style="font-size: 27px; padding-left: 64px;"></span>
                                    </li>
                                </a>
                            </ul>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </section>
    <!-- Content Area -->

    <!-- services section -->
    <section id="services" class="service-area">
        <div class="container" style=" display: flex; justify-content: center; align-items: start;flex-wrap: wrap;">
            <form id="form">
                <div class="row">
                    <h2 class="block_title">請上傳PDF檔</h2>
                    <h3>請上傳財務報表</h3>
                    <h5>請注意若是檔案內為掃描檔會讓AI無法判讀，在使用人工智慧技術時，應謹慎考慮其潛在的錯誤判斷風險。請細心使用，並對產生的結果進行審慎評估。</h5>

                    <input type="file" class="form-control" name="pdf" id="pdf" style="margin: 9px 0px 0px 0px;">
                    <div id="upload-status" style="display: none;"></div>

                    <button class="btn btn-outline-secondary" type="button" onclick="uploadFile()" style="margin: 20px 0px 5px 0px; border: 3px solid #000;border-radius: 20px; color: #000;">送出</button>
                    <input type="text" class="form-control" name="message" id="message">
                    <button class="btn btn-outline-secondary" type="button" onclick="chat()" style="margin: 20px 0px 5px 0px;border: 3px solid #000;border-radius: 20px;color: #000;">發送消息</button>
                    <br>
                    <div id="chat-zone"></div>
                    <br>
                    <div class="snap">
                        <div class="quencard">
                            <h1 class="hh1">或許你想問</h1>
                            <div class="cloum">
                                <?php
                                foreach ($terms as $term => $formula) {
                                    echo '<p onclick="fillInput(this)" class="Press" data-formula="' . htmlspecialchars($formula) . '">' . htmlspecialchars($term) . '</p>';
                                }
                                ?>
                                <p>&nbsp;</p>
                            </div>
                        </div>

                    </div>
            </form>
        </div>
    </section>

    <section id="portfolio" class="portfolio-area">
        <div class="container" style="display: flex;text-align: center;">
            <div class="row port cs-style-3">

            </div>
        </div>
    </section>

    <!-- Footer Area -->

    <!-- <footer>
        <div class="container">
            <div class="row">
                <div class="col-sm-6">
                    <p class="copyright">© 樹德科大 版權所有 <a href="#" target="_blank">Your Website Link</a></p>
                </div>
                <div class="col-sm-6">
                    <p class="designed">Theme by <a href="http://themewagon.com" target="_blank">Themewagon</a></p>
                </div>
            </div>
        </div>
    </footer> -->

    <!-- Necessery scripts -->
    <script src="assets/js/jquery-2.1.3.min.js"></script>
    <script src="assets/js/bootstrap.min.js"></script>

    <script src="assets/js/jquery.actual.min.js"></script>
    <script src="assets/js/smooth-scroll.js"></script>
    <script src="assets/js/owl.carousel.js"></script>
    <script src="assets/js/script.js"></script>
    <script src="assets/js/modernizr.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>

    <script>
        let sourceId;
        var gptCount = 1;
        const chatZone = document.querySelector('#chat-zone');
        let messages = [];
        const messageDom = document.querySelector("#message");
        messageDom.addEventListener("keydown", function(event) {
            if (event.key === "Enter") {
                event.preventDefault();
                chat();
            }
        });

        // Helper function to display upload status
        function displayStatus(message, isSuccess) {
            const statusElement = document.getElementById('upload-status');
            statusElement.textContent = message;
            statusElement.style.color = isSuccess ? 'green' : 'red'; // Green for success, red for errors
            statusElement.style.display = 'block'; // Make sure the element is visible
        }

        function uploadFile() {

            const pdf = document.querySelector('#pdf').files[0];
            const formData = new FormData();
            formData.append("file", pdf);
            console.log("test:" + formData);
            fetch('https://api.chatpdf.com/v1/sources/add-file', {
                method: 'POST',
                body: formData,
                headers: {
                    "x-api-key": "sec_XqI9fuUZe3NZctUAdQeLKVtvt2A8bbjg",
                },
            }).then(async res => {
                const response = await res.json();
                if (res.ok) {
                    alert("成功");
                    sourceId = response.sourceId;
                    displayStatus('PDF上传成功', true); // Display success message
                } else {
                    alert("失敗");
                    throw new Error(`上传失败: ${res.status} ${res.statusText}`);
                }
            }).catch(error => {
                console.error("Error:", error);
                displayStatus(error.message, false); // Display error message
            });
        }

        function chat() {
            console.log(gptCount);
            gptCount++;
            if (gptCount == 5) {
                gptCount = 1;
                uploadFile();

            }
            let memory = [{
                    "role": "user",
                    "content": "你是一個財經專家"

                },

            ]

            let message = messageDom.value;
            messages.push({
                "role": "user",
                "content": message
            });


            chatZone.innerHTML += `user: ${message}<br><br>`;
            const data = {
                sourceId: sourceId,
                messages: messages
            };

            messageDom.value = "";
            axios.post("https://api.chatpdf.com/v1/chats/message", data, {
                    headers: {
                        "x-api-key": "sec_XqI9fuUZe3NZctUAdQeLKVtvt2A8bbjg",
                        "Content-Type": "application/json",
                    },
                })
                .then((response) => {
                    messages.push({
                        "role": "assistant",
                        "content": response.data.content
                    });
                    chatZone.innerHTML += `assistant: ${response.data.content}<br><br>`;
                })
                .catch((error) => {
                    console.error("Error:", error);
                    displayStatus('Error: ' + error.message, false); // Display error message
                });
        }

        function fillInput(element) {
            // 獲取輸入框元素
            var inputElement = document.getElementById('message');
            // 將詞句的內容填入輸入框
            var formula = element.getAttribute('data-formula');
            inputElement.value = formula;
            chat();
        }
    </script>

</body>

</html>