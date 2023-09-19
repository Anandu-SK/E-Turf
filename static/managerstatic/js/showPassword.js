function showPassword()
{
    var passwd = document.getElementById("form3Example4");

    if (passwd.type === "password")
    {

        passwd.type = "text";
    }
    else{

        passwd.type = "password";
    }
}