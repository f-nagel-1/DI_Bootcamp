// //*Add the lastname Smith to the object
// Change the price of the pear, so it will contain the Taxes
// Ask the user for the fruit he wants between Apple, Banana and Pear. Make sure that your code accept all type of strings, for example "Banana" or "banana" or "BaNaNA"
// Console.log the price for the specific fruit the user wants*//

let userCart = {
	username : "John",
	password: 1234,
	isUserSignedIn : true,
	cart : {
		apple : 2,
		banana : 1,
		pear : 5
	},
	prices : {
		apple : 0.5,
		banana : 0.8646466363,
		pear : 0.2
	}
};

//1. Add the lastname Smith to the object
userCart["lastname"] = "Smith";
console.log(userCart);


// Change the price of the pear, so it will contain the Taxes
userCart.["prices"]["pear"] = userCart.["prices"]["pear"] * 1,17;

OR
userCart.["prices"]["pear"] *= 1,17;


// 3.  Ask the user for the fruit he wants between Apple, Banana and Pear. Make sure that your code accept all type of strings, for example "Banana" or "banana" or "BaNaNA"
// Console.log the price for the specific fruit the user wants*//


let choice = prompt("What do you want").toLowerCase();
console.log(userCart["prices"][choice]);



////4. Change the price of banana, round it 2 numbers avec the comma

// let userCart = {
// 	username : "John",
// 	password: 1234,
// 	isUserSignedIn : true,
// 	cart : {
// 		apple : 2,
// 		banana : 1,
// 		pear : 5
// 	},
// 	prices : {
// 		apple : 0.5,
// 		banana : 0.8646466363,
// 		pear : 0.2
// 	}
// };
let roundbanana = userCart["prices"]["banana"];
console.log(roundbanana.toFixed(2));
