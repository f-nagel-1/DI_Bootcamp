
//
// For each of the questions, find 2 WAYS of accessing :
//
// 1. The div DOM node?
//
// 2. The ul DOM node?
//
// 3. The second li (with Pete)?

let divElement = document.body.firstElementChild
document.body.children[0]

OR
let ulElement = divElement.nextElementSibling;
document.body.lastElementChild
document.body.children[1]

let liElement = ulElement.lastElementChild;
document.body.lastElementChild.lastElementChild
document.body.children[1].lastElementChild
document.body.children[1].children[1]


change content:

liElement.textContent += "Smith"
