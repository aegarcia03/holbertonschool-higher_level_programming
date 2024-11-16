// Select the HTML element where the character name will be displayed
const character = document.getElementById("character");
// Fetch data from the SWAPI API
fetch("https://swapi-api.hbtn.io/api/people/5/?format=json")
    .then(response => {
        if(!response.ok) {
              // Check if the response is OK (status 200-299)
            throw new Error(`Response status: ${response.status}`);
        }
        return response.json(); //Parse the JSON data from the response
    })
    .then(data => {
        // Handle any errors that occur during the fetch

        character.textContent = data.name;

    })
    .catch(error => {
        // Handle any errors that occur during the fetch
        console.error("Error fetching data", error);
        character.textContent = "Failed to load character.";
    });
