// //
// Exercise 1: Simple If/Else Statement
// Create 2 variables, x and y. Each of them should have a different numeric value.
// // Write an if/else statement that checks which number is bigger.

let x = 100;
let y = 51332;

if (x > y){
    console.log("X is bigger")
}
else{
    console.log("Y is bigger")
}

// ֽExercise 2: Chihuahua
// Instructions
// Create a variable called newDog where it’s value is “Chihuahua”.
// Check and display how many letters are in newDog.
// Display the newDog variable in uppercase and then in lowercase (no need to create new variables, just console.log twice).
// Check if the variable newDog is equal to “Chihuahua”
// if it does, display ‘I love Chihuahuas, it’s my favorite dog breed’
// else, console.log ‘I dont care, I prefer cats’


var newDog = "Chihuahua";
console.log(newDog.length);
console.log(newDog.toUpperCase());
console.log(newDog.toLowerCase())

// Check if the variable newDog is equal to “Chihuahua”
// if it does, display ‘I love Chihuahuas, it’s my favorite dog breed’
// else, console.log ‘I dont care, I prefer cats’

var newDog = "Chihuahua";

if (newDog === "Chihuahua"){
    console.log("I love Chihuahuas, it’s my favorite dog breed")
} else{
    console.log("I dont care, I prefer cats")

}


//
// Exercise 3: Even Or Odd
// Instructions
// Prompt the user for a number and save it to a variable.
// Check whether the variable is even or odd.
// If it is even, display: “x is an even number”. Where x is the actual number the user chose.
// If it is odd, display: “x is an odd number”. Where x is the actual number the user chose.
