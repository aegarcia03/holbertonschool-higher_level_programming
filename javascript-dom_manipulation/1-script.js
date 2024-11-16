const header = document.querySelector("header");
const red_header = document.querySelector("#red_header");

function updatecolor() {
    header.style.color = "#FF0000";
}

red_header.addEventListener("click", updatecolor);