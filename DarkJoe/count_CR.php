<!DOCTYPE html>

<html class="no-js " lang="ZH_TW">

<head>
    <title>計算炭權</title>
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
    <link rel="stylesheet" href="assets/css/nav.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">



    <style>
        h2 {
            text-align: center;
            color: #3737a7;
        }

        p {
            text-align: center;
            font-size: 20px;
            margin: 10px 5px 20px 5px;
        }
    </style>


</head>

<body id="body">



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




    <section id="services" class="service-area">
        <div class="container">
            <h2>請輸入過去12個月的使用情形</h2>
            <div class="row">
                <div class="col-md-2">
                    <p>電力使用<br>(Electricity)</p>
                    <div class="input-group mb-3" style="display: flex; justify-items: center;flex-direction: row;justify-content: center;">
                        <input type="number" name="Electricity" id="Electricity" style="width: 100px;" oninput="calculateEmissions()">
                    </div>
                    <p>度/年<br>(Kwh/Year)</p>

                </div>
                <div class="col-md-2">
                    <p>車用汽油<br>(Gasoline)</p>
                    <div class="input-group mb-3" style="display: flex; justify-items: center;flex-direction: row;justify-content: center;">
                        <input type="number" name="Gasoline" id="Gasoline" style="width: 100px;" oninput="calculateEmissions()">
                    </div>
                    <p>公升/年<br>(Liter/Year)</p>
                </div>
                <div class="col-md-2">
                    <p>柴油使用<br>(Diesel)</p>
                    <div class="input-group mb-3" style="display: flex; justify-items: center;flex-direction: row;justify-content: center;">
                        <input type="number" name="Diesel" id="Diesel" style="width: 100px;" oninput="calculateEmissions()">
                    </div>
                    <p>公升/年<br>(Liter/Year)</p>
                </div>
                <div class="col-md-3">
                    <p>天然氣使用<br>(Natural Gas)</p>
                    <div class="input-group mb-3" style="display: flex; justify-items: center;flex-direction: row;justify-content: center;">
                        <input type="number" name="Natural" id="Natural" style="width: 100px;" oninput="calculateEmissions()">
                    </div>
                    <p> 度/年<br>(m3/Year)</p>
                </div>
                <div class="col-md-3">
                    <p>桶裝瓦斯使用<br>(Liquefied Petroleum Gas)</p>
                    <div class="input-group mb-3" style="display: flex; justify-items: center;flex-direction: row;justify-content: center;">
                        <input type="number" name="Liquefied" id="Liquefied" style="width: 145px;" oninput="calculateEmissions()">
                    </div>
                    <p>公升/年<br>(Liter/Year)</p>
                </div>
            </div>
        </div>
    </section>

    <section id="portfolio" class="portfolio-area">
        <div class="container" style="background-color: chocolate;">
            <h2>碳排計算量</h2>
            <p style="text-align: center;margin: 0 0 30px 0;">(GHG emissions calculation)<br>單位:公噸 CO2e/年(Unit: tonnes
                CO2e/Year)</p>
            <div class="row">
                <div class="col-md-2">
                    <p>電力<br>(Electricity)</p>

                    <div id="elect" class="count">0</div>
                </div>
                <div class="col-md-2">
                    <p>車用汽油<br>(Gasoline)</p>
                    <div id="car" class="count">0</div>
                </div>
                <div class="col-md-2">
                    <p>柴油使用<br>(Diesel)</p>
                    <div id="diesel" class="count">0</div>
                </div>
                <div class="col-md-3">
                    <p>天然氣使用<br>(Natural Gas)</p>
                    <div id="naturl" class="count">0</div>
                </div>
                <div class="col-md-3">
                    <p>桶裝瓦斯使用<br>(Liquefied Petroleum Gas)</p>
                    <div id="liquefied" class="count">0</div>
                </div>
            </div>
        </div>
    </section>

    <section id="intro">
        <div class="container">
            <h2>總額</h2>
            <p style="text-align: center;margin: 0 0 30px 0;">(Total GHG emissions)</p>
            <p>單位:公噸 CO2e/年<br>(Unit: tonnes CO2e/Year)</p>
            <div class="row">
                <div class="col-md-12">
                    <div id="total" class="count">0</div>
                    <p>&nbsp;</p>
                    <p>&nbsp;</p>
                </div>

                <div class="col-md-5">
                    <p>&nbsp;</p>
                    <h2>相當於消耗</h2>
                </div>
                <div class="col-md-2">
                    <div id="forest" class="count">0</div>
                </div>
                <div class="col-md-5">
                    <p>&nbsp;</p>
                    <h2>公頃森林</h2>
                </div>
                <p>&nbsp;</p>
                <p>依農委會推估，每公頃森林1年固碳量為15公噸</p>
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
    <script src="https://maps.googleapis.com/maps/api/js?v=3.exp"></script>
    <script src="assets/js/jquery.actual.min.js"></script>
    <script src="assets/js/smooth-scroll.js"></script>
    <script src="assets/js/owl.carousel.js"></script>
    <script src="assets/js/script.js"></script>
    <script src="assets/js/count.js"></script>
    <script>
        // 在页面加载后自动滚动到指定位置
        
    </script>
</body>

</html>