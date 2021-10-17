////spent 2h on this, still doesn't work and I don't know why...

function createPlanets(){
    let planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"];
    for (let i = 0; i < planets.length; i++){
        let divPlanet = document.createElement('div');
        divPlanet.classList.add("classOf", planets[i]);

        let nameOfPlanet = document.createTextNode(planets[i]);
        divPlanet.appendChild(nameOfPlanet);

        let parentSection = document.getElementsByClassName("listPlanets");
            parentSection.appendChild(divPlanet);
    }
}

createPlanets()
