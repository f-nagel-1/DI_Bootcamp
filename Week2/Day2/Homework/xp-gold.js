///Exercise 1 : The World Translator

let language = prompt("what is your language?");
let languageLower = language.toLowerCase();

if (languageLower === "french"){
    alert("Bonjour")
} else if (languageLower === "english") {
    alert("hello")
} else if (languageLower === "hebrew") {
    alert("Shalom")
} else {
    alert("01110011 01101111 01110010 01110010 01111001")
}

///Exercise 2 : The Grade Assigner

let grade = prompt("what is your grade?");

if (grade > 90){
    console.log("A")
} else if ((grade > 80) && (grade <= 90)) {
    console.log("B")
} else if ((grade >= 70) && (grade <= 80)) {
    console.log("C")
} else {
    console.log("D")
}



// Exercise 3 : Verbing

let verb = prompt("give me a verb");

if ((verb.length >= 3) && (!verb.endsWith("ing")) ){
    console.log(verb.concat("ing"))
} else if ((verb.length >= 3) && (verb.endsWith("ing")) ){
    console.log(verb.concat("ly"))
} else {
    console.log(verb)
}
