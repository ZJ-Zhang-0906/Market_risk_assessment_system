
//countGP 計算綠能 ZJ 2024/01/10

//=============================數值=============================
var taiwanCities = {
    "基隆市": 2.22, // 每日發電量一度
    "台北市": 3.31,
    "新北市": 3.0,
    "桃園市": 2.99,
    "新竹市": 3.21,
    "新竹縣": 3.15,
    "苗栗縣": 3.26,
    "台中市": 3.46,
    "彰化縣": 3.46,
    "南投縣": 3.23,
    "雲林縣": 3.42,
    "嘉義市": 3.07,
    "嘉義縣": 3.22,
    "台南市": 3.38,
    "高雄市": 3.25,
    "屏東縣": 3.18,
    "宜蘭縣": 3.06,
    "花蓮縣": 3.32,
    "台東縣": 3.66,
    "澎湖縣": 3.35,
    "金門縣": 3.28,
    "連江縣": 3.49
};
//=================================================================


//=======================網頁載入==================================
$(document).ready(function () {
    // 初始化縣市選擇為'基隆市'並觸發 change 事件
    $('#city').val('基隆市').change();

    // 當縣市選擇改變時，更新每日發電量的顯示
    $('#city').on('change', function () {
        var selectedCity = $(this).val(); // 獲取選中的縣市的 key
        var generationValue = taiwanCities[selectedCity]; // 從 taiwanCities 對象中獲取相對應的發電量值
        // 更新 DOM 元素以顯示選中的城市的每日發電量
        $('#someElementId').text(selectedCity+"平均日發電量"+generationValue);
    });
});


//========================計算================================================================
function calculator() {
    var rangeValue = parseFloat($('#customRange1').val());
    var selectedCity = $('#city').val();
    var cityGenerationParameter = taiwanCities[selectedCity] || 0;
    var sellingElectricityValue = parseFloat($('#SellingElectricity').val()) || 0;
    var systemSetingValue = parseFloat($('#Systemseting').val()) || 0;

    // 執行計算
    var capacity = rangeValue * 0.3; // 可裝設容量
    var annualGenerationCapacity = capacity * (cityGenerationParameter * 365); // 預估每年發電量
    var annualIncome = sellingElectricityValue * annualGenerationCapacity; // 預估電能躉售年收入
    var recycle = systemSetingValue / (annualIncome || 1); // 粗估回收年限，避免除以0
    var co2 = annualGenerationCapacity * 0.509; // 預估每年CO2減量

    // 更新DOM元素
    $('#capacity').text(capacity.toFixed(0));
    $('#AnnualGenerationCapacity').text(annualGenerationCapacity.toFixed(0));
    $('#Annualincome').text(annualIncome.toFixed(0));
    $('#Recycle').text(recycle.toFixed(2)); // 保留兩位小數
    $('#Co2').text(co2.toFixed(0));
}
//================================================================

//============================網頁載入====================================
$(document).ready(function () {
    // 初始化城市選擇為'基隆市'並觸發相應的更新
    $('#city').val('基隆市').trigger('change');

    $('#customRange1').val(300);
    // 在 #setrange 顯示滑塊的初始值
    $('#setrange').text($('#customRange1').val());
    // 當範圍桿桿改變時更新顯示的值
    $("#customRange1").on("input", function () {

        $("#setrange").text($(this).val());
    });

    // 當系統設置價格輸入框的值改變時，更新顯示在卡片上的值
    $("#Systemseting").on("input", function () {
        var systemSetingValue = parseFloat($(this).val()) || 0;
        $("#SystemSettings").text(systemSetingValue.toFixed(0));
    });

    // 為相關元素添加事件監聽器以實時更新計算結果
    $('#customRange1, #city, #SellingElectricity, #Systemseting').on('input change', calculator);

    // 頁面加載時執行一次計算以初始化值
    calculator();
});



//=============================我是countGP底部=============================





//================================================================================================================================================================================================


//countCR 計算炭權  ZJ 2024/01/10
window.onload = function () {
    var targetElement = document.getElementById('container'); // 指定要滚动到的元素
    if (targetElement) {
        targetElement.scrollIntoView({
            behavior: 'smooth'
        });
    }
};

function calculateEmissions() {
    var electricityUsage = parseFloat(document.getElementById('Electricity').value) || 0;
    var gasolineUsage = parseFloat(document.getElementById('Gasoline').value) || 0;
    var dieselUsage = parseFloat(document.getElementById('Diesel').value) || 0;
    var naturalUsage = parseFloat(document.getElementById('Natural').value) || 0;
    var liquefiedUsage = parseFloat(document.getElementById('Liquefied').value) || 0;

    var electricityEmissions = electricityUsage * 0.000496;
    var gasolineEmissions = gasolineUsage * 0.002362;
    var dieselEmissions = dieselUsage * 0.00265;
    var naturalEmissions = naturalUsage * 0.00188;
    var liquefiedEmissions = liquefiedUsage * 0.001754;

    document.getElementById('elect').innerText = electricityEmissions.toFixed(2);
    document.getElementById('car').innerText = gasolineEmissions.toFixed(2);
    document.getElementById('diesel').innerText = dieselEmissions.toFixed(2);
    document.getElementById('naturl').innerText = naturalEmissions.toFixed(2);
    document.getElementById('liquefied').innerText = liquefiedEmissions.toFixed(2);

    // Calculate the total emissions and return the value
    var totalEmissions = electricityEmissions + gasolineEmissions + dieselEmissions + naturalEmissions + liquefiedEmissions;
    document.getElementById('total').innerText = totalEmissions.toFixed(2);
    var forestEmissions = totalEmissions / 15;
    document.getElementById('forest').innerText = forestEmissions.toFixed(2);
}
//=============================我是countCR底部=============================


//=================================================================================================================================================================================================