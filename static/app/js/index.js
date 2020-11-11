// let headers = new Headers();

// headers.append("Content-Type", "application/json");
// headers.append("Accept", "application/json");

// headers.append(
//     "Access-Control-Allow-Origin",
//     "https://cors-anywhere.herokuapp.com/https://ipleak.net/json/"
// );
// headers.append(
//     "Access-Control-Allow-Origin",
//     "https://cors-anywhere.herokuapp.com/https://deywuro.com/api/sms"
// );

// // headers.append(
// //     "Access-Control-Allow-Origin",
// //     "http://127.0.0.1:5000/data"
// // );

// headers.append("Access-Control-Allow-Credentials", "true");

//variables
// var phone = document.getElementById('phone');
// var radioButton = document.getElementById("radio-b");
// var button = document.getElementById("btn");

// $.get("https://ipleak.net/json/", function(data, status){
//     console.log(data);

//     if(data['country_name'] === "Ghana"){
//         console.log();
//         } else {
//         window.location.href = "forbidden.html";
//         }

// });

// // SEND SMS
// $(document).ready(function() {
//     $("#telForm").submit(function(e) {
//         e.preventDefault();

//     var phone = document.forms["telForm"]["phone"].value;
//     if (phone == ""){
//         alert("Phone Number is Required");
//     }
//     else {
//     $.ajax({
//         method: "GET",
//         // headers: headers,
//         url: "https://cors-anywhere.herokuapp.com/https://deywuro.com/api/sms",
//         crossDomain: true,
//         contentType: "application/json",
//         data: {
//             "username": "sammy",
//             "password": "suppORT_pass_0987",
//             "source": "Test",
//             "destination": String(phone),
//             "message": String(otp)
//             },
//         dataType: "json",
//         success: function (data) {
//             console.log(data);
//             alert("OTP sent. Click OK and then Next to proceed.");
//         },
//         error: function (err) {
//         console.log("ERROR: ",err);
//         },
//     });
    
//     // window.location = "survey.html";
// }
//     e.preventDefault();
// });
//    });

