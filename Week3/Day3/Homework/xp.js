//exercise 1

//step 1- name function + retrieve element to animate

function myMove(){
    let cube = document.getElementById("animate");


/// step 2 set starting position. 0 here refers to the start of the parent div container, i.e. the top left corner

    let startPos = 0;


//step 3 set interval of action to be executed. Interval always needs a: function, b: miliseconds. !

    let frequency = setInterval(moveStart, 10);

// step 4 define moveStart function. parent container dimension = 400

function moveStart(){
    if (startPos === 350){
        clearInterval(frequency);
    }else {
        startPos++;

    } cube.style.left = startPos + 'px';

}

}
