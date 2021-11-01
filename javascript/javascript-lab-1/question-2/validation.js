// Selectors
var signUpForm = document.forms['signForm'];
var inputName = document.getElementById('name');
var inputEmail = document.getElementById('email');
var inputPhone = document.getElementById('phone');
var inputPassword = document.getElementById('password');
var errorMssg = document.getElementsByTagName('p');

// Regular Expressions
var regName = /^[^0-9]{3,}$/;
var regEmail = /^\S+@+\S+$/;
var regPhone = /^[0-9]{10,}$/;
var regPassword = /^\S{6,}$/;

// Functions

function validateForm(e) {
	e.preventDefault();

	var fullName = inputName.value.trim();
	var emailId = inputEmail.value.toLowerCase().trim();
	var phoneNo = inputPhone.value.trim();
	var passWord = inputPassword.value.trim();

	if (!regName.test(fullName)) {
		errorMssg[0].innerHTML = "Enter valid full name.";
		inputName.focus();
	} else if (!regEmail.test(emailId)) {
		errorMssg[1].innerHTML = "Enter valid email address.";
		inputEmail.focus();
	} else if (!regPhone.test(phoneNo)) {
		errorMssg[2].innerHTML = "Enter valid phone number.";
		inputPhone.focus();
	} else if (!regPassword.test(passWord)) {
		errorMssg[3].innerHTML = "Enter valid password.";
		inputPassword.focus();
	} else {
		errorMssg[4].innerHTML = "Your Submission has been sent."
		// signUpForm.submit();
	}

	// remove error message
	if (regName.test(fullName)) {
		errorMssg[0].innerHTML = "";
	} 
	if (regEmail.test(emailId)) {
		errorMssg[1].innerHTML = "";
	} 
	if (regPhone.test(phoneNo)) {
		errorMssg[2].innerHTML = "";
	} 
	if (regPassword.test(passWord)) {
		errorMssg[3].innerHTML = "";
	}
}
