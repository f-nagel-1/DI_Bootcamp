//exercise 1

let socialNetworkNavigation = document.getElementById("navBar").setAttribute("id", "socialNetworkNavigation");

let newLi = document.createElement("li");
let logout = document.createTextNode("Logout");
    newLi.appendChild(logout);

let ulList = document.body.firstElementChild.firstElementChild;
    ulList.appendChild(newLi);


====


document.getElementsByClassName("list")[0].lastElementChild.textContent = "Richard";
--
document.getElementsByClassName("list")[0].firstElementChild.textContent = "Elena";

document.getElementsByClassName("list")[1].firstElementChild.textContent = "Elena";

--

let newLi1 = document.createElement("li");
let student1 = document.createTextNode("Hey students");
    newLi1.appendChild(student1);

document.getElementsByClassName("list")[0].appendChild(newLi1);
document.getElementsByClassName("list")[1].appendChild(newLi1);

--
document.getElementsByClassName("list")[1].children[1].textContent = ""



______



document.body.firstElementChild.style.backgroundColor = "blue";
document.body.firstElementChild.style.padding = "20px";

document.body.children[1].firstElementChild.textContent = "";
document.body.children[1].lastElementChild.style.border = "thick solid #0000FF";

document.body.style.fontSize = "x-large";
