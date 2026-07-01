const menuButton = document.getElementById("menu-btn");
const sidebar = document.getElementById("sidebar");

menuButton.addEventListener("click", () => {

    sidebar.classList.toggle("collapsed");

});