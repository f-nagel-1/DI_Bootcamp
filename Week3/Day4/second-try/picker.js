
// let colorGrid = document.getElementById("grid-container");

//
// for (let i )


var data = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"],
    ["10", "11", "12"]
  ];

 function addCells(){
    let container = document.getElementById("grid-container");
  for (let i of data)
    { for (let j of i)
        {
    let cellsBlock = document.createElement("div");
    cellsBlock.innerHTML = j;
    cellsBlock.className = "cell";
    container.appendChild(cellsBlock);
  }}
};

addCells();


let cells = document.getElementsByClassName("cell");
let colors = ['blue','purple','DarkGoldenRodgrey','black','red','green','yellow','brown', 'orange', 'pink', 'silver', 'lightgrey'];

let index = 0;

function colorPallete(){
    for (let element of cells){
        element.style.backgroundColor = colors[index++];
    }
}
colorPallete();


function drawingGrid(){}
for(var i = 0; i < 25; i++) {
    var row = document.createElement("div");
    for(var j = 0; j< 61; j++) {
        var drawingCell = document.createElement("div");
        row.appendChild(drawingCell);
        drawingCell.className = "drawingCells";
    }
    document.getElementById("drawingArea").appendChild(row);
    console.log("drawing cells created")
}

drawingGrid();
