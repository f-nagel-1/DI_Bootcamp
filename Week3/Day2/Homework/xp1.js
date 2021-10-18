///exercise 1

let articleParent = document.body.firstElementChild;
    articleParent.removeChild(articleParent.lastElementChild);

---
let h2Header = document.getElementsByTagName("h2")[0];
    h2Header.addEventListener("click", h2ColorChange);

function h2ColorChange(){
    h2Header.style.backgroundColor = "red";
}

----

let h1Header = document.getElementsByTagName("h1")[0];
let randomNr = Math.floor(Math.random() * 101);

h1Header.style.fontSize = (randomNr + "px" );

---

let h3Header = document.getElementsByTagName("h3")[0];
    h3Header.addEventListener("click", hideH3);

function hideH3(){
        h3Header.style.display = "none";
    }

----

let button = document.getElementById("btn");
    button.addEventListener("click", makeBold);

let allPs = document.getElementsByTagName("p");

function makeBold(event){
    for (let i = 0; i < allPs.length; i++){
    allPs[i].style.fontWeight = "bold";
    }
}





----

// Exercise 2 : Transform The Sentence
Instructions
Add this sentence to your HTML file then follow the steps :

<p><strong>Hello</strong> I hope you are enjoying <strong>this</strong> class. At the
<strong>end</strong> you <strong>will</strong> be great Developers!
<strong>Enjoy</strong> the <strong>JavaScript </strong> lessons</p>


Create a function called getBold_items() that takes no parameter. This function should collect all the bold items inside the paragraph.
Create a function called highlight() that changes the color of all the bold text to blue.
Create a function called return_normal() that changes the color of all the bold text back to black.
Call the function highlight() onmouseover (ie. when the mouse pointer is moved onto the paragraph), and the function return_normal() onmouseout (ie. when the mouse pointer is moved out of the paragraph). Look at this example
