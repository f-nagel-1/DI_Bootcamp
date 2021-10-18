
function createButton(){
    let colors = ["blue", "yellow", "green", "pink"];
    for (let i = 0; i < colors.length; i++){
        let button = document.createElement("button");
        let buttonText = document.createTextNode(colors[i]);
        button.appendChild(buttonText);
        document.body.firstElementChild.appendChild(button);
//adds listener that looks out for "click" action AND if it happens executes function "changeColor"
        button.addEventListener("click", changeColor);
    }
}
createButton()

function changeColor(event){
    console.log(event.target);
    let color = event.target.textContent.toLowerCase();
    document.body.style.backgroundColor = color;

}


//
//
// function changeColor(event){
//     let color = event.target.textContent.toLowerCase();
//     document.body.style.backgroundColor=color;
//
// }
//
// 3. Each button should have an "click" event listener that
// changes the background color of the document,  to the color of the button (do it directly in the JS)
//
// Example:
// when you click on the YELLOW button, it should change the document
// background color to yellow
