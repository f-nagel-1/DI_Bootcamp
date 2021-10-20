// //
//
// ## SECOND PART : GAME
//
//
// * the first section and the second section need to be created using Javascript
//
// 	* FIRST SECTION:
// 	the first section, we need an array of colors. And we need a loop, that does 8*3 iterations and create a new div in each iteration. In each iteration we assign a color to the div (ie. the color is retrieved from the array of colors)
//
// 	* SECOND SECTION: And we need a loop, that does 60*24 iterations and create a new div in each iteration
//
//
// ## Javascript
// 	* PALLET
// 		* Inside the loop where you created the div, we need to add an event listener to each div. Event listener of "click" that calls a callback function
// 		`div.addEventListener("click", getColor)`
// 		* getColor that takes an event parameter
// 			* it retrieves the backgroundColor of the target
// 			* save the backgroundColor in a global variable named `myColor`
//
// 	* GRID (painting)
// 		* FIRST FEATURE
//
// 		Inside the loop where you created the div of the grid, we need to add an event listener to each div. Event listener of "click" that calls a callback function
// 		`div.addEventListener("click", setColor)`
// 			* setColor that takes an event parameter
// 				* use the value of the `myColor` global variable and assign it to the backgroundColor of the square I click on (ie. event.target)
//
//
// 		* SECOND FEATURE
// 			* As long as the mouse is pressed AND moving => paint the squares
// 			* use the mousedown event
// 			* use the mouseover event
// 			* use the mouseup event
//
// 				* add event listeners to the squares of mousedown and mouseover
//
// 				* When the mousedown event is executed we create a variable named `isMouseDown` that is set to true
//
// 				* When the mouseup event is executed we create a variable named `isMouseDown` that is set to false
//
// 				* When the mouseover event is executed we check the value of the `isMouseDown` variable. If the `isMouseDown` variable is equal to true, => then I change the background color of the squares.
//
// 		* THIRD FEATURE: click on the "clear button", it clears the square
// 		* when you click on the button, the background color of each square should change to white.
// 			* `button.addEventListener("click", deleteColors)`
// 				* In the deleteColors function, I do a loop trhough all the div of the grid, and change the background color of each square to white.

let colorBoxes = document.getElementsByClassName("grid-item") ;

let colors = [""]


"BurlyWood",
"CadetBlue"
"Chartreuse"
"Chocolate"
"Coral"
"Cornsilk"
"Crimson"
"Cyan"
"DarkCyan"
"DarkGoldenRod"
"DarkGrey"
"DarkGreen"
"DarkKhaki"
"DarkMagenta"

DarkOliveGreen

DarkOrange
DarkOrchid
#9932CC
DarkRed
#8B0000
