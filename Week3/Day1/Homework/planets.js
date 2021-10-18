

function createPlanets(){
    let planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"];

    // getElementsbyClassName will give me all the elements => turn out a list rather than 1 specific element with this class name. Here I am looking for the parent which is the section <section class="listPlanets">. So here I want the first one, hence why I need to add the index. => [0] after the name of the class name
    let parentSection = document.getElementsByClassName("listPlanets")[0];


//// or document.querySelector(."listPlanets") works because the querySelector picks the very first item that matches the description of listPlanets


    let colors =['blue','purple','pink','black','red','green','yellow','brown']


    for (let i = 0; i < planets.length; i++){
        let divPlanet = document.createElement('div');

        //adds the class for styling html in round sphere
        divPlanet.classList.add('planet');
        // why divPlanet.classList.add(planets[i]); necessary???

        let nameOfPlanet = document.createTextNode(planets[i]);
        divPlanet.append(nameOfPlanet);

        parentSection.append(divPlanet);

        divPlanet.style.color ='white';
        divPlanet.style.backgroundColor = colors[i];

    }
}

createPlanets()
