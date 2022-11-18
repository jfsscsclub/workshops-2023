var num1 = document.getElementById("num1");
var num2 = document.getElementById("num2");
var result = document.getElementById("result")

// to get content inside the element
num1 = Number(num1.innerHTML);
num2 = Number(num2.innerHTML);

function add() {
    result.innerHTML = num1 + num2;
}


function subtract() {
    result.innerHTML = num1 - num2;
}
function divide() {
    result.innerHTML = num1 / num2;
}

function multiply() {
    result.innerHTML = num1 * num2;
}
