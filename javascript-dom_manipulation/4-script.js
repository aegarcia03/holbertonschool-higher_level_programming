const add_item = document.getElementById("add_item");
const my_list = document.querySelector("ul.my_list");

add_item.addEventListener("click", addNewListItem);

function addNewListItem() {
    const new_item = document.createElement("li");
    new_item.textContent = "Item";

    my_list.appendChild(new_item);
}
