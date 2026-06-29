/*
=========================================
Login Handler
=========================================
*/

const loginForm = document.querySelector("#loginForm");

if (loginForm) {

    loginForm.addEventListener("submit", async (event) => {

        event.preventDefault();

        const payload = {

            email:
            document.querySelector("#email").value,

            password:
            document.querySelector("#password").value

        };

        try {

            const response = await fetch("/api/auth/login", {

                method: "POST",

                headers: {

                    "Content-Type": "application/json"

                },

                body: JSON.stringify(payload)

            });

            if (response.ok) {

                window.location = "/dashboard";

            }

            else {

                alert("Invalid credentials.");

            }

        }

        catch (error) {

            console.error(error);

        }

    });

}