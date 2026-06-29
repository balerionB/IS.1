/*
==================================================
Global JavaScript

This file contains JavaScript shared by the entire
application.
==================================================
*/

// Wait until the HTML page has fully loaded.
document.addEventListener("DOMContentLoaded", () => {

    console.log("PS-SRMS Frontend Initialized");

    // Future global features:
    // - Sidebar toggle
    // - Toast notifications
    // - Theme switching
    // - Live notification polling
});
/*
==========================================
Responsive Sidebar Toggle
==========================================
*/

const sidebar = document.querySelector(".sidebar");
const toggleButton = document.querySelector("#sidebarToggle");

if (toggleButton) {

    toggleButton.addEventListener("click", () => {

        sidebar.classList.toggle("show");

    });

}
if (password.length < 8) {

    alert("Password must contain at least 8 characters.");

    return;

}