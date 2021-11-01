// Selectors

const resultBtn = document.getElementById('btn');
const firstNumber = document.getElementById('firstInput');
const secondNumber = document.getElementById('secondInput');
const operator = document.getElementById('dropDown');
const output = document.querySelector('.result');

// Event Listeners

resultBtn.addEventListener('click', validation);

// Regular Expression

var regCheck = /^[+|-]?[0-9]*[.]?[0-9]*$/;

// Functions

// Function for validation
function validation(e) {
	e.preventDefault();
	var firstNo = firstNumber.value;
	var secondNo = secondNumber.value;
	if ((!regCheck.test(firstNo)) || (firstNo == "")) {
		output.innerHTML = 'Enter a valid first number';
		output.style.color = '#ED0000';
		firstNumber.focus();
	} else if ((!regCheck.test(secondNo)) || (secondNo == "")) {
		output.innerHTML = 'Enter a valid second number';
		output.style.color = '#ED0000';
		secondNumber.focus();
	} else {
		output.innerHTML = 'Result is: ' + calculation(firstNo, secondNo);
		output.style.color = '#008000';
	}
}

// Function for calculation
function calculation(num1, num2) {
	var num1 = Number(num1);
	var num2 = Number(num2);
	var result;
	switch(operator.value) {
		case "+":
		result = num1 + num2;
		break;
		case "-":
		result = num1 - num2;
		break;
		case "*":
		result = num1 * num2;
		break;
		case "/":
		result = num1 / num2;
		break; 
	}
	return result;
}