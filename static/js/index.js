
  setTimeout(function () {
    document.getElementById("btn").click();
  }, 300);
// toggle  between login and signup view on clicking LOGIN option in the template
  function logindisplay() {
    var loginmodal = document.getElementById("loginmodal")
    loginmodal.style.display = "block";
    var signupmodal = document.getElementById("signupmodal")
    signupmodal.style.display = "none";
    document.getElementById("signup").classList.remove("btn-danger");
    document.getElementById("login").classList.add("btn-danger");
  }

// toggle  between login and signup view on clicking SIGNUP option in the template
  function signupdisplay() {
    document.getElementById("signupmodal").style.display = "block";
    document.getElementById("loginmodal").style.display = "none";
    document.getElementById("signup").classList.add("btn-danger");
    document.getElementById("login").classList.remove("btn-danger");
  }

// toggle  between login and signup view on clicking FORGOT PASSWORD option in the template
  function Reset_link() {
    var reset_link = document.getElementById("reset_link")
    reset_link.style.display = "block";
    loginmodal.style.display = "none";
    signupmodal.style.display = "none";
    document.getElementById("header").innerHTML = "Enter Registered Email for Reset link"
  }
  var email2 = document.getElementById("email2");
  if (email2.value != "") {
    loginmodal.style.display = "block";
    signupmodal.style.display = "none";
    reset_link.style.display = "none";
    document.getElementById("signup").classList.remove("btn-danger");
    document.getElementById("login").classList.add("btn-danger");
  }

// toggle  between login signup and reset options if email is invalid for reset link
  var email1 = document.getElementById("email1");
  if (email1.value != "") {
    loginmodal.style.display = "none";
    signupmodal.style.display = "block";
    reset_link.style.display = "none";
    document.getElementById("signup").classList.add("btn-danger");
    document.getElementById("login").classList.remove("btn-danger");
  }

// showing alert for invalid credentials and vanishes after 4 sec
  setTimeout(function () {
    document.getElementById("invalid_credentials").style.display = "none";
  }, 4000)

  var email3 = document.getElementById("email3").value;
  var reset_link = document.getElementById("reset_link");
  if (email3 != "") {
    loginmodal.style.display = "none";
    signupmodal.style.display = "none";
    reset_link.style.display = "block";
    document.getElementById("header").innerHTML = "Enter Registered Email for Reset link"
    setTimeout(function () {
      document.getElementById("alert_for_reset_password").style.display = "none";
    }, 4000)
  }

  var check_email = document.getElementById("check_email");
  if (check_email) {
    alert("Check your email to Reset your Password & come back to Login again")
  }
