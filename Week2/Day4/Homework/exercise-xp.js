// Exercise 1 Information


function infoAboutMe(){
    console.log("My name is and I am 100 years old")
}
infoAboutMe()


//Part 2

function infoAboutPerson(personName, personAge, personFavoriteColor) {
    console.log(`Your name is ${personName}, you are ${personAge} years old, your favorite color is ${personFavoriteColor}`)
}

infoAboutPerson("David", 45, "blue")
infoAboutPerson("Josh", 12, "yellow")



//Part 3


function infoAboutPerson(personName, personAge, personFavoriteColor, personHobbies) {
    for (let i = 0; i < personHobbies.length; i++){
        console.log(`Your name is ${personName}, you are ${personAge} years old, your favorite color is ${personFavoriteColor} and your hobbies are ${personHobbies}`) }
    }

infoAboutPerson("David", 45, "blue", ["tennis", "painting"])




////Exercise 2 Keyless Car

let age = parseInt(prompt("What is your age?"))

function checkDriverAge(age){
    if (age < 18){
        alert("Sorry, you are too young to drive this car. Powering off")
    }
    else if (age > 18){
        alert("You are old enough to drive, Powering On. Enjoy the ride!")
    }
    else if (age == 18){
        alert("Congratulations on your first year of driving. Enjoy the ride!")
    }
    else {
        alert("Please enter a number")
    }
}


checkDriverAge(17)



// Exercise 3


function checkNumber(){
    for (let i = 0; i < 101; i++){
        if (i%2 == 0){
            console.log("The number", i, "is even")
        }
        else {
            console.log(">The number", i, "is uneven")
        }
    }
}
checkNumber()



//Exercise 4: Find The Numbers Divisible By 23



function isDivisible(){
    let sum = 0;
    for (let i = 0; i < 501; i++){
        if (i%23 == 0){
            console.log(i);
            sum += i;
        }
    } return sum;
}
isDivisible()



// Exercise 5 : Amazon Shopping

let amazonBasket = {
    glasses: 1,
    books: 2,
    floss: 100
}

let item = prompt("what do you want?")

function checkBasket(){
    for (let i in amazonBasket){
        if (item in amazonBasket){
            console.log("Item is in the basket")
        }
        else {
            console.log("sorry, nothing. try again")
        }
    }


}

checkBasket()



//
// Exercise 7 : Shopping List

/// it gives me 49.50 for some reason???


//2 conditions =>
// if item in stock, add it to sum?


let stock = {
    "banana": 6,
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}

let prices = {
    "banana": 4,
    "apple": 2,
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
}

let shoppingList = ["banana", "orange", "apple"];

let sum = 0;

function myBill(){
    // goes through each element in the array => get banana = 0
    for (let i = 0; i < shoppingList.length; i++){
        //if it is bigger than 0, then loop over second object to check the key value pair
        for (let i in stock){
            if (stock[i] > 0){
                sum += prices[i];
            }
        }
    }return sum;


}
myBill()


////Exercise 8

let bill = parseInt(prompt("What is your bill?"))

function calculator(){
    if (bill < 50){
        let tip = bill * 0.2;
        console.log("The tip amout is", tip, "and the final bill is:", bill + (bill * 0.15))}
    else if (bill > 50 && bill < 200){
        console.log("The tip amout is:", bill * 0.15, "and the final bill is:", bill + (bill * 0.15))}
    else{
        console.log("The tip amout is:", bill * 0.10, "and the final bill is:", bill + (bill * 0.10))}

}
calculator()



// Exercise 9 : Vacations Costs

let numberNights = parseInt(prompt("number of nights in the hotel?"))
let sumNights;

function hotelCost(){
    while (numberNights.length === 0){
        numberNights = prompt("number of nights in the hotel?")
    }
    let sumNights = (numberNights * 140)
    return sumNights;
}
hotelCost()



let destination = prompt("where to?").toLowerCase();
let priceLocation = 0;

function planeRideCost(){
    while (destination.length === 0){
        destination = prompt("where to?")
    }
        if (destination === "london"){
            priceLocation = 183;
        }
        else if (destination === "paris"){
            priceLocation = 220;
        }
        else {
            priceLocation = 300;
        }
        return priceLocation;
}

planeRideCost()


Define a function called rentalCarCost().
It should ask the user for the number of days they would like to rent the car.
If the user doesn’t answer or if the answer is not a number, ask again.
Calculate the cost to rent the car. The car costs $40 everyday.
If the user rents a car for more than 10 days, they get a 5% discount.
The function should return the total price of the car rental.
Define a function called totalVacationCost() that returns the total cost of the user’s vacation by calling the 3 functions that you created above.
Example : The car cost: $x, the hotel cost: $y, the plane tickets cost: $z.
Hint: You have to call the functions hotelCost(), planeRideCost() and rentalCarCost() inside the function totalVacationCost.
Call the function totalVacationCost()
Bonus: Instead of using a prompt inside the 3 first functions, only use a prompt inside the totalVacationCost() function.
