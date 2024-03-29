// document.addEventListener('DOMContentLoaded', function() {
//     document.getElementById('QueryButton').addEventListener('click', function(e) {
//       e.preventDefault();
  
//       var formData = new FormData();
//       formData.append('companyName', document.getElementById('Company_Name').value);
//       formData.append('companyID', document.getElementById('Uniform_numbers').value);
  
//       fetch('http://localhost/testtdb/DarkJoe/Risk_Assessment-search.php', {
//           method: 'POST',
//           body: formData
//       })
//       .then(response => response.text())
//       .then(data => {
//           if (data.trim() === "1") {
//                 window.location.href = '/../../Risk_end.php';
//           } else {
//               console.error('爬虫失败或返回了非预期的值');
//           }
//       });
//     });
//   });
  