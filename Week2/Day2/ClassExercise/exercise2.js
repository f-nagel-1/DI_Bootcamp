// //1. If the user is SignedIn - show him his name and password
// 2. If not - alert the user "you need to sign in"


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

//dont't need to write === true because it will be evluated anyway
//  ! at the beginning shows "if untrue"

if (userCart["isUserSignedIn"]) {
    console.log(userCart["username"], userCart["password"])
} else {
    alert("You need to sign in")
}



//
// 1. If the user is John AND his password is 1234 - alert him "You are signed in"

if (userCart["username"] === "John" && userCart["password"] === "1234") {
    alert ("You are signed in")
}


// 2. If the user is John OR his password is 1234 - alert him "One credential is false"

let userCart = {
	username : "John",
	password: 1234,
	isUserSignedIn : true

};

if (userCart["username"] === "John" && userCart["password"] === 1234) {
    alert("You are signed in")
} else if (userCart["username"] === "John" || userCart["password"] === 1234) {
    alert("one credential is wrong")
}else{
    alert("You need to sign in")
}

// 3. Else,alert the user "you need to sign in"
