// Exercise
// let names = ["John", "Lola", "Tom"];
// 1. Create a function that adds the name of each students to
// a paragraph
// 2. each paragraph needs to be background yellow, font-size 25px
// 3. Add the 3 paragraph to the div already on the page
// 12:37
// <div id="container"></div>



function createParagph(){

    let names = ["John", "Lola", "Tom"];
    for (let i = 0; i < names.length; i++){
        // 1. create 3 paragraphs and give the variable name "par"
        let par = document.createElement("p");
        // 2. style all the paragraphs
        par.style.backgroundColor = "yellow";
        par.style.fontSize = "25px";
        // 3. create 3 text nodes, each one corresponding to the name => names[i]
        let text = document.createTextNode(names[i]);
        // 4. add the nodes of the names to each paragrph
        par.appendChild(text);
        //5. link them to the parent called "div"
        let container = document.getElementById("container");
        container.appendChild(par);
    }

}

createParagph();
