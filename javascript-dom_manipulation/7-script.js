const list_movies = document.getElementById("list_movies");

fetch("https://swapi-api.hbtn.io/api/films/?format=json")
    .then(response => {
        if(!response.ok) {
            throw new Error(`Response status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        // Loop through the results and create list items for each movie title
        data.results.forEach(movie =>
            {
                const listItem = document.createElement("li");  // Create a new list item
                listItem.textContent = movie.title; // Set its text content to the movie title
                list_movies.appendChild(listItem); // Append the list item to the UL
            });
    })
    .catch(error => {
        // Handle any errors that occur during the fetch
        console.error("Error fetching data", error);
        list_movies.textContent = "Failed to load movie titles.";
    });
