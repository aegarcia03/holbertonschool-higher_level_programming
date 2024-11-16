const header = document.querySelector("header");
const red_header = document.getElementById("red_header");

red_header.addEventListener("click", addRedClassToHeader)

function addRedClassToHeader() {
    header.classList.add("red");
}