/*
===========================================
Citizen Request Submission
===========================================
*/

const requestForm =
document.querySelector("#requestForm");

if(requestForm){

requestForm.addEventListener("submit",async(e)=>{

e.preventDefault();

/* Collect form values */

const payload={

title:
document.querySelector("#title").value,

department_id:
document.querySelector("#department").value,

priority:
document.querySelector("#priority").value,

description:
document.querySelector("#description").value

};

/* Send data to backend */

const response=await fetch(

"/api/requests",

{

method:"POST",

headers:{

"Content-Type":"application/json"

},

body:JSON.stringify(payload)

}

);

/* Redirect after success */

if(response.ok){

window.location="/citizen/dashboard";

}

});

}