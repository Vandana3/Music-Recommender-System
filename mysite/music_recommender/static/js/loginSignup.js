$(document).ready(function() {
// On Click SignIn Button Checks For Valid E-mail And All Field Should Be Filled
$("#login").click(function() {
if ($("#loginusername").val() == '' || $("#loginpassword").val() == '') {
alert("Please enter all fields");
}
});

$("#register").click(function() {
if ($("#name").val() == '' || $("#registerusername").val() == '' || $("#registerpassword").val() == '' || $("#registeremail").val() == '') {
alert("Please enter all fields");
}
});
// On Click SignUp It Will Hide Login Form and Display Registration Form
$("#signup").click(function() {
$("#first").slideUp("slow", function() {
$("#second").slideDown("slow");
});
});
// On Click SignIn It Will Hide Registration Form and Display Login Form
$("#signin").click(function() {
$("#second").slideUp("slow", function() {
$("#first").slideDown("slow");
});
});
});