window.addEventListener("scroll",function(){

    const navbar=document.querySelector(".public-navbar");

    if(window.scrollY>60){

        navbar.style.background="#084298";

    }

    else{

        navbar.style.background="#0B5ED7";

    }

});
window.addEventListener("load",()=>{

document.querySelector(".hero-title")
.style.opacity="1";

});