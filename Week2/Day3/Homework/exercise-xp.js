//Exercise 1 : Your Favorite Colors

let colors = ["green", "red", "blue", "purple"];
let numbers = ["1st", "2nd", "3rd", "4th"];


for (let i = 0; i < colors.length; i++) {
    console.log('My ' + numbers[i] + ' choice is ' + colors[i]);
    }



// let colors = ["green", "red", "blue", "purple"];
//
//
// for (let i = 0; i < colors.length; i++) {
//     console.log('My #' + (i+1) + ' choice is ' + colors[i]);
//     }





//
// List Of People

// Write code to make a copy of the people array using slice. The copy should NOT include “Mary” or your name.
// Write code that console.logs Mary’s index. take a look at indexOf on google.
// Write code that gives the indexOf “Foo” (this should return -1). Why does it return -1
// Create a variable called last which value is the last element of the array.
// Hint: What is the relationship between the index of the last element in the array and the length of the array?



let people = ["Greg", "Mary", "Devon", "James"];
//removes Greg = > "Mary", "Devon", "James"
people.shift();

//replace “James” to “Jason” = "Mary", "Devon", "Jason"
people.splice(2, 1, "Jason");
//add Elena at end => "Mary", "Devon", "Jason", Elena
people.push("Elena");


// console log each person, after Jason end
for (let i = 0; i < 3; i++){
    console.log(people[i]);
    }

let peopleWitoutMary = people.shift();
console.log(peopleWitoutMary);


let peopleCopy = peopleWitoutMary.slice(0);
    console.log(peopleCopy);
