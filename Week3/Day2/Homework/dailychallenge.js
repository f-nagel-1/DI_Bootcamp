let inputs = document.getElementsByTagName('input');

let button = document.getElementById("lib-button");
    button.addEventListener("click", addInputs);


let arrWords = [];

function addInputs(event){
    event.preventDefault();
    let noun = document.getElementById("noun").value;
    arrWords.push(noun);
    let adjective = document.getElementById("adjective").value;
    arrWords.push(adjective);
    let person = document.getElementById("person").value;
    arrWords.push(person);
    let verb = document.getElementById("verb").value;
    arrWords.push(verb);
    let place = document.getElementById("place").value;
    arrWords.push(place);

    console.log(arrWords);


    let storyParagraph = document.createElement("p");

    for (let i = 0; i < arrWords.length; i++){
        // let text = document.createTextNode(arrWords[i]);
        let spanElement = document.getElementById("story");

        storyParagraph.innerHTML =
        "The" + " " + adjective + " " + noun + " told " + person + " to " + verb + " in " + place ;
       spanElement.appendChild(storyParagraph);
    }

}


 //
 //
 // for (let input of inputs) {
 //    alert( input.value + ': ' + input.checked );
 //  }
