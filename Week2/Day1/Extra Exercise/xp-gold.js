///Exercise 1

let me = ["my","favorite","color","is","blue"];
console.log(me.join(" "));


///Exercise 2

let str1 = "mix";
let str2 = "pod";

let new1 = str1.replace("x", "d");
let new2 = str2.replace("d", "x");
let space = " ";
let newphrase = str2.concat(space, str1);
console.log(newphrase);


///Exercise 3

let num1 = parseInt(prompt("Pick a first number"));
let num2 = parseInt(prompt("Pick a second number"));
alert(num1 + num2);


///3 Bonus

let num1 = parseInt(prompt("Pick a first number"));
let num2 = parseInt(prompt("Pick a second number"));
let calc = (prompt("What do you want to do? + - / or *"));
if (calc === "+") {
    alert(num1 + num2);
}
else if (calc === "-") {
    alert(num1 - num2);
}

else if (calc === "/") {
    alert(num1 / num2);
}

else  {
    alert(num1 * num2);
}
