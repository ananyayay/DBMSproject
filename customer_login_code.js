function formSubmitted()
{
    var e = document.getElementById("emailinput").value;
    var p = document.getElementById("passwordinput").value;
    if (e.toLowerCase()=="customer@coldmail.com" && p=="customer123")
        window.alert("Succesfully logged in");
    else
        window.alert("Incorrect Email Id or Password");
}