let boldSelect = document.getElementsByTagName("strong");
// have to make empty array when working with getElementsByTagName as they are plural AND you want to select all the elements there, not just one. if wanted one, make [] after the strong
let boldWords = [];

// can't use use (let i = 0; i < boldSelect.length; i++) because you are working with array


DOESNT WORK:

let arr = ["a", "b"]
let boldSelect = document.getElementsByTagName("strong");
let boldWords = [];


// here the i in this loop gives me only the number of the index, but not actually the content of the position. this is why I have to change it to boldSelect[i])
function getBold_items(){
    for (let i = 0; i < boldSelect.length; i++){
        boldWords.push(boldSelect[i].textContent);
}   console.log(boldWords);
}
getBold_items();


WORKS. why??

let boldSelect = document.getElementsByTagName("strong");
let boldWords = [];

// let elem of => gives me the actual content, this is why I do not need an i there.

function getBold_items(){
    for (let elem of boldSelect){
        boldWords.push(elem.textContent);
}   console.log(boldWords);
}
getBold_items();



function highlight(){
    let boldItems = document.body.firstElementChild.lastElementChild.getElementsByTagName("strong");
    boldItems.style.color = "magenta";
}

highlight();
