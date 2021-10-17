//1. create function called playgame ask user if want to play.
    // if false = by
    // else = ok
    //     enter another if loop

function confirmFunction(){
    if (confirm("Do you want to play a game?")){
        return true;
    }else{
        alert("ok, no problem");
        return false;
    }
}



function userNumber(){
    if (!confirmFunction())
        return;
    let userInput = parseInt(prompt("Enter number between 0 and 10"));
        if (isNaN(userNumber)){
            alert("Sorry Not a number, Goodbye");
            return;
        } else if (userNumber > 10){
            alert("Sorry it’s not a good number, Goodbye");
            return;
        } return userInput;
}

// playTheGame();



function playGame(){

    let humanNr = userNumber();
    let computerNumber = Math.floor(Math.random() * 11);

    // for (let i = 1; i <= 4; i++){
        if (humanNr === computerNumber){
            alert("WINNER");
      } else if (humanNr > computerNumber) {
          alert("Your number is bigger, guess again");
      } else if (humanNr < computerNumber) {
          alert("Your number is smaller, guess again");
      }

    }
// }

playGame();



//
//
//
// In the JS file, create a function called playTheGame() that takes no parameter.
// In the function, start by asking the user if they would like to play the game (Hint: use the built-in confirm() function).
//
// If the answer is false, alert “No problem, Goodbye”.
//
// If his answer is true, follow these steps:
// Ask the user to enter a number between 0 and 10 (Hint: use the built-in prompt() function). You then have to check the validity of the user’s number :
//
// If the user didn’t enter a number (ie. if he entered another data type) alert “Sorry Not a number, Goodbye”.
// If the user didn’t enter a number between 0 and 10 alert “Sorry it’s not a good number, Goodbye”.
// Else (ie. he entered a number between 0 and 10), create a variable named computerNumber where the value is a random number between 0 and 10 (Hint: Use the built-in Math.random() function). Make sure that the number is rounded.
