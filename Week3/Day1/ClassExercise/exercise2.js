// For each of the questions, find 2 WAYS to access :
//
// 1. The div node

document.body.firstElementChild
document.body.children[0]
let divContainer = document.getElementById("container");


// 2. The ul nodes, and render all of it's children one by one
//
document.getElementsByTagName("ul")
document.getElementsByClassName("list")
document.querySelectorAll(".list")

// 3. The first li of each ul

let ulElement = document.getElementsByTagName("ul");

for (let ul of ulElement){
    console.log(ul.children[0].textContent)
}
