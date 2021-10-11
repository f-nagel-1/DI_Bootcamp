///Exercise 1

let sentence = prompt("Give me a sentence");
let keyword = "nemo";

if (sentence.includes(keyword)) {
    let position = sentence.indexOf("nemo");
    alert("I found Nemo at the position Nr: " + position);
}

else  {
    alert("I cant find Nemo");
}


//Exercise 3
