let inputs = document.getElementsByTagName('input');

let button = document.getElementById("lib-button");
    button.addEventListener("click", addInputs);
    button.addEventListener("click", storyTime);

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


}

function storyTime(event){
    let story = document.createElement("p");

}


 //
 //
 // for (let input of inputs) {
 //    alert( input.value + ': ' + input.checked );
 //  }
