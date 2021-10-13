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
