<?php
$jsonFilePath = 'C:/xampp/htdocs/Market_risk_assessment_system/DarkJoe/data.json'; //替换为你想要保存的路径

// 檢查文件是否存在
if (file_exists($jsonFilePath)) {
    $jsonData = file_get_contents($jsonFilePath);
    $dataArray = json_decode($jsonData, true);
} else {
    $dataArray = [];
    // 處理文件不存在的情況，例如通過錯誤訊息
    echo "<p>找不到數據文件。</p>";
}
?>
<!DOCTYPE html>
<!--[if lt IE 7]>      <html class="no-js lt-ie9 lt-ie8 lt-ie7"> <![endif]-->
<!--[if IE 7]>         <html class="no-js lt-ie9 lt-ie8"> <![endif]-->
<!--[if IE 8]>         <html class="no-js lt-ie9"> <![endif]-->
<!--[if gt IE 8]><!-->

<html class="no-js " lang="ZH_TW"> <!--<![endif]-->

<head>
    <title>結果</title>
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
    <link rel="stylesheet" href="assets/css/owl.carousel.css">
    <link rel="stylesheet" href="assets/css/owl.theme.css">
    <link rel="stylesheet" href="assets/css/animate.css">
    <link rel="stylesheet" href="assets/css/style.css">
    <link rel="stylesheet" href="assets/css/risk.css">
    <link rel="stylesheet" href="assets/css/nav.css">

    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">




</head>

<body id="body">
    <!--[if lt IE 7]>
                <p class="browsehappy">You are using an <strong>outdated</strong> browser. Please <a href="http://browsehappy.com/">upgrade your browser</a> to improve your experience.</p>
        <![endif]-->

    <!-- Header area -->


    <!-- Navigation area -->
    <section id="navigation">
        <div class="container">
            <div class="row">
                <div class="col-xs-2" style=" font-size: x-large; display: flex; ">
                    <a href="index.php">
                        <i><span class=" pe-7s-home in"></span>
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
                                <a href="FinancialTest.php">
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
        <div class="container">
            <div class="row" id="END">
                <div id="warning">請注意:風險評估結果可能會出錯。請考慮核對重要資訊。<br>底部會有我們的風險評分規則及等級。</div>
                <div id="riskResult">
                    <div id="companyInfo"></div>
                    <div class="line"></div>
                    <div id="result"> <?php
                                        // 讀取 JSON 檔案
                                        $json = file_get_contents('C:\xampp\htdocs\Market_risk_assessment_system\DarkJoe\respon.json'); //這是openai 回傳的檔案替换为你想要保存的路径
                                        $data = json_decode($json, true);
                                        // 將內容以 HTML 格式顯示
                                        $response = nl2br($data['response']); // 將換行符號轉換為 <br>
                                        echo "<p>{$response}</p>";
                                        ?></div>
                </div>


            </div>
        </div>
        </div>

    </section>
    <br>
    <br>
    <br>
    <br>
    <div class="row mt-5">
        <section id="risk_rule_table" class="portfolio-area">
            <h2 class="text-center">以下為我們的風險評分規則及風險等級</h2>
            <table id="assetLiabilityTable" class="table table-bordered ">
                <thead class="thead-dark fs-2 text-center">
                    <tr>
                        <th scope="col">項目</th>
                        <th scope="col">情況</th>
                    </tr>
                </thead>
                <tbody class="fs-2 text-center">
                    <tr>
                        <td>資本額</td>
                        <td>增加+1分<br>減少-1分</td>
                    </tr>
                    <tr>
                        <td>負責人</td>
                        <td>變更-1分<br>不變更+0分</td>
                    </tr>
                    <tr>
                        <td>地址</td>
                        <td>變更-1分<br>不變更+0分</td>
                    </tr>
                    <tr>
                        <td>開發票</td>
                        <td>有開+1分<br>沒開-1分</td>
                    </tr>
                    <tr>
                        <td>是否營業</td>
                        <td>營業中+1分<br>沒營業-1分</td>
                    </tr>
                    <tr>
                        <td>訴訟</td>
                        <td>沒訴訟+1分<br>有訴訟-1分</td>
                    </tr>
                    <tr>
                        <td>勞基法</td>
                        <td>沒違法+1分<br>有違法-1分</td>
                    </tr>
                    <tr>
                        <td>環保法</td>
                        <td>沒違法+1分<br>有違法-1分</td>
                    </tr>
                    <tr>
                        <td>是否有動產</td>
                        <td>沒有+1分<br>有-1分</td>
                    </tr>
                </tbody>
            </table>
            <table class="table table-bordered fs-2">
                <tr>
                    <th>風險評分標準</th>
                    <th>0分以下</th>
                    <th>1分</th>
                    <th>2分</th>
                    <th>3分</th>
                    <th>4分</th>
                    <th>5分</th>
                    <th>6分</th>
                    <th>7分</th>
                </tr>
                <tr>
                    <td></td>
                    <td>高風險</td>
                    <td>高風險</td>
                    <td>中高風險</td>
                    <td>中高風險</td>
                    <td>中低風險</td>
                    <td>中低風險</td>
                    <td>低風險</td>
                    <td>低風險</td>
                </tr>
            </table>
        </section>

    </div>







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
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-p34f1UUtsS3wqzfto5wAAmdvj+osOnFyQFpp4Ua3gs/ZVWx6oOypYoCJhGGScy+8" crossorigin="anonymous"></script>
    <script>
        // 在页面加载后自动滚动到指定位置
        window.onload = function() {
            var targetElement = document.getElementById('container'); // 指定要滚动到的元素
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        };

        fetch('data.json')
            .then(response => response.json()) // 解析 JSON
            .then(data => {
                // 從 JSON 數據中提取各部分的第一條記錄
                const pyMoeaInput = data.py_moea_input[0];
                const prtrData = data.py_prtr_input[0];
                // 查找 SerialNumber 为数字的记录
                const molInput = data.py_mol_input.find(item => !isNaN(parseInt(item.SerialNumber, 10)));
                const ppstrqInput = data.py_ppstrq_input.find(item => !isNaN(parseInt(item.SerialNumber, 10)));

                // const molInput = data.py_mol_input.find(item => item.SerialNumber === "1");
                // const ppstrqInput = data.py_ppstrq_input.find(item => item.SerialNumber === 1);
                const twincnData = data.twincn[0];

                let content =
                    '統編號碼: ' + pyMoeaInput.BusinessAccountingNO + '<br>' +
                    '<span class="companyInfo"> 公司名稱: ' + pyMoeaInput.CompanyName + '</span>' +
                    '<span class="companyInfo"> 資本額: ' + pyMoeaInput.CapitalStockAmount + '</span>' +
                    '<span class="companyInfo"> 實收資本額: ' + pyMoeaInput.PaidInCapitalAmount + '</span>' +
                    '<span class="companyInfo"> 負責人姓名: ' + pyMoeaInput.ResponsibleName + '</span>' +
                    '<span class="companyInfo"> 公司位置: ' + pyMoeaInput.CompanyLocation + '</span>' +
                    '<span class="companyInfo"> 環保是否有裁罰: ' + prtrData.NumberOfData + '</span>' +
                    '<span class="companyInfo"> 司法是否有裁罰: ' + twincnData.Lawsuit + '</span>';
                // 檢查勞動違規裁罰信息
                // 检查劳动违规裁罚信息
                if (molInput && parseInt(molInput.SerialNumber, 10) !== 0) {
                    content += '<span class="companyInfo">勞動違規裁罰: 有，罰鍰字號為 ' + molInput.PenaltyFontSize + '違規內容: ' + molInput.IllegalLawsAndRegulations + '</span>';
                } else {
                    content += '<span class="companyInfo">無勞動違規裁罰</span>';
                }

                // 检查动产抵押信息
                if (ppstrqInput && parseInt(ppstrqInput.SerialNumber, 10) !== 0) {
                    content += '<span class="companyInfo">動產抵押: 有，狀態為 ' + ppstrqInput.CaseStatus + '</span>';
                } else {
                    content += '<span class="companyInfo">無動產抵押</span>';
                }

                // 將結果顯示在網頁上
                document.getElementById('companyInfo').innerHTML = content;
            })
            .catch(error => {
                // 處理錯誤情況
                console.error('錯誤獲取或解析 JSON 檔案', error);
            });
        // fetch('respon.json')
        //     .then(response => response.json()) // 解析 JSON
        //     .then(data => {
        //         // 从 JSON 数据中提取 "response" 的值
        //         const result = data.response;
        //         // 将提取的值插入到 HTML 中
        //         document.getElementById('result').innerHTML = result;
        //     })
        //     .catch(error => {
        //         console.error('Error fetching the JSON file:', error);
        //     });
    </script>
</body>

</html>