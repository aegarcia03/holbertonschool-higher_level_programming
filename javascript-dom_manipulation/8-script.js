document.addEventListener("DOMContentLoaded", () => {
    const hello = document.getElementById("hello"); 
});


fetch("https://hellosalut.stefanbohacek.dev/?lang=fr")
    .then(response => {
        if(!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        hello.textContent = json.hello;

    })
    .catch(error => {
        // Handle any errors that occur during the fetch
        console.error("Error fetching data", error);
        hello.textContent = "Failed to load translation";
    });
