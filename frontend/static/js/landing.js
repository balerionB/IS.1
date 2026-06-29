/*
====================================
Landing Page JavaScript
====================================
*/

// Animate statistics cards on hover.

document.querySelectorAll(".card-custom")

.forEach(card => {

card.addEventListener("mouseenter", () => {

card.style.transform="translateY(-6px)";

});

card.addEventListener("mouseleave", () => {

card.style.transform="translateY(0px)";

});

});