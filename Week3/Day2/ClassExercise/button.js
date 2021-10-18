let redButton = document.getElementById("red");
let blueButton = document.getElementById("blue");

blueButton.addEventListener("click", function (event){
    let color = event.target.textContent.toLowerCase();
    document.body.style.backgroundColor=color;

});

redButton.addEventListener("click", function (event){
    let color = event.target.textContent.toLowerCase();
    document.body.style.backgroundColor=color;

});

// redButton.addEventListener("click", function(){
//      document.body.style.background = "red";
//
// });


// blueButton.addEventListener("click", function(){
//      document.body.style.background = "blue";
//
// });
