---
layout: page 
title: Login
permalink: /login
search_exclude: true
menu: nav/home.html
show_reading_time: false 
---

<style>
.login-container {
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap; /* allows the cards to wrap onto the next line if the screen is too small */
}

.login-card {
    margin-top: 0; /* remove the top margin */
    width: 45%;
    border: 1px solid #ddd;
    border-radius: 5px;
    padding: 20px;
    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3);
    margin-bottom: 20px;
    overflow-x: auto; /* Enable horizontal scrolling */
}

.login-card h1 {
    margin-bottom: 20px;
}

.signup-card {
    margin-top: 0; /* remove the top margin */
    width: 45%;
    border: 1px solid #ddd;
    border-radius: 5px;
    padding: 20px;
    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3);
    margin-bottom: 20px;
    overflow-x: auto; /* Enable horizontal scrolling */
}

.signup-card h1 {
    margin-bottom: 20px;
}

</style>

<div class="login-container">
    <!-- Python Login Form -->
    <div class="login-card">
        <h1 id="pythonTitle">User Login (Python/Flask)</h1>
        <form id="pythonForm" onsubmit="pythonLogin(); return false;">
            <p>
                <label>
                    GitHub ID:
                    <input type="text" name="uid" id="uid" required>
                </label>
            </p>
            <p>
                <label>
                    Password:
                    <input type="password" name="password" id="password" required>
                </label>
            </p>
            <p>
                <button type="submit">Login</button>
            </p>
            <p id="message" style="color: red;"></p>
        </form>
    </div>
    <div class="signup-card">
        <h1 id="signupTitle">Sign Up</h1>
        <form id="signupForm" onsubmit="signup(); return false;">
            <p>
                <label>
                    Name:
                    <input type="text" name="name" id="name" required>
                </label>
            </p>
            <p>
                <label>
                    GitHub ID:
                    <input type="text" name="signupUid" id="signupUid" required>
                </label>
            </p>
            <p>
                <label>
                    Password:
                    <input type="password" name="signupPassword" id="signupPassword" required>
                </label>
            </p>
            <p>
                <label>
                    <input type="checkbox" name="kasmNeeded" id="kasmNeeded">
                    Kasm Server Needed
                </label>
            </p>
            <p>
                <button type="submit">Sign Up</button>
            </p>
            <p id="signupMessage" style="color: green;"></p>
        </form>
    </div>
</div>

<script type="module">
    import { login, pythonURI, fetchOptions } from '{{site.baseurl}}/assets/js/api/config.js';

    // Function to handle Python login
    window.pythonLogin = function() {
        const options = {
            URL: `${pythonURI}/api/authenticate`,
            callback: pythonDatabase,
            message: "message",
            method: "POST",
            cache: "no-cache",
            body: {
                uid: document.getElementById("uid").value,
                password: document.getElementById("password").value,
            }
        };
        login(options);
    }

    // Function to handle signup
    window.signup = function() {
    const signupButton = document.querySelector(".signup-card button");

    // Disable the button and change its color
    signupButton.disabled = true;
    signupButton.style.backgroundColor = '#d3d3d3'; // Light gray to indicate disabled state

    const signupOptions = {
        URL: `${pythonURI}/api/user`,
        method: "POST",
        cache: "no-cache",
        body: {
            name: document.getElementById("name").value,
            uid: document.getElementById("signupUid").value,
            password: document.getElementById("signupPassword").value,
            kasm_server_needed: document.getElementById("kasmNeeded").checked,
        }
    };

    fetch(signupOptions.URL, {
        method: signupOptions.method,
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(signupOptions.body)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`Signup failed: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        document.getElementById("signupMessage").textContent = "Signup successful!";
        // Optionally redirect to login page or handle as needed
        // window.location.href = '{{site.baseurl}}/profile';
    })
    .catch(error => {
        console.error("Signup Error:", error);
        document.getElementById("signupMessage").textContent = `Signup Error: ${error.message}`;
        // Re-enable the button if there is an error
        signupButton.disabled = false;
        signupButton.style.backgroundColor = ''; // Reset to default color
    });
}


    // Function to fetch and display Python data
    function pythonDatabase() {
        const URL = `${pythonURI}/api/id`;

        fetch(URL, fetchOptions)
            .then(response => {
                if (!response.ok) {
                    throw new Error(`Flask server response: ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                window.location.href = '{{site.baseurl}}/profile';
            })
            .catch(error => {
                console.error("Python Database Error:", error);
                const errorMsg = `Python Database Error: ${error.message}`;
            });
    }

    // Call relevant database functions on the page load
    window.onload = function() {
         pythonDatabase();
    };
</script>


<!-- OURS -->
<!-- 
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login Page</title>
    <link rel="stylesheet" href="styles.css">
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            color: #191970;
        }
        .container {
            background-color: white;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            width: 300px;
            color: #191970;
        }
        .login-form {
            display: flex;
            flex-direction: column;
            color: #191970;
        }
        .input-group {
            margin-bottom: 15px;
            color: #191970;
        }
        label {
            margin-bottom: 5px;
            color: #191970;
        }
        input {
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 3px;
        }
        button {
            padding: 10px;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 3px;
            cursor: pointer;
        }
        button:hover {
            background-color: #0056b3;
        }
        .signup-section {
            margin-top: 20px;
            border-top: 1px solid #ccc;
            padding-top: 10px;
            color: #191970;
        }
        /* Smaller button styles */
        .small-button {
            padding: 5px;
            font-size: 10px; /* Adjust font size as needed */
            width: 70px; /* Set a specific width */
            align-self: left; /* Center the small button */
        }
        /* Modal styles */
        .modal {
            display: none;
            position: fixed;
            z-index: 1;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            overflow: auto;
            background-color: rgba(0, 0, 0, 0.5);
            color: #191970;
        }
        .modal-content {
            background-color: white;
            margin: 15% auto;
            padding: 20px;
            border: 1px solid #888;
            width: 300px;
            border-radius: 5px;
        }
        .close {
            color: #aaa;
            float: right;
            font-size: 28px;
            font-weight: bold;
        }
        .close:hover,
        .close:focus {
            color: black;
            text-decoration: none;
            cursor: pointer;
        }
        .status {
            font-size: 10;
            color: #006400;
        }
    </style>
</head>
<body>
    <div class="container">
        <form class="login-form" onsubmit="return false;"> <!-- Prevent default submission -->
            <h2>Login</h2>
            <div class="input-group">
                <label for="username">Username: </label>
                <input type="text" id="username" name="username" required>
            </div>
            <div class="input-group">
                <label for="password">Password: </label>
                <input type="password" id="password" name="password" required> <!-- where password is hidden -->
            </div>
            <p id="status"></p> <!-- Correct closing tag -->
            <br>
            <button onclick="checking_accesablilty()" type="button">Login</button> <!-- Change to type="button" -->
            <br>
            <button type="button" id="signupBtn" class="small-button">Sign Up</button>
        </form>
    </div>
    <!-- The pop-up -->
    <div id="signupModal" class="modal">
        <div class="modal-content">
            <span class="close" id="closeModal">&times;</span>
            <h2>Sign Up</h2>
            <form class="signup-form">
                <div class="input-group">
                    <label for="new-username">Create Username: </label>
                    <input type="text" id="new-username" name="new-username" required>
                </div>
                <div class="input-group">
                    <label for="new-password">Create Password: </label>
                    <input type="password" id="new-password" name="new-password" required>
                </div>
                <button type="submit">Sign Up</button>
            </form>
        </div>
    </div>
    <script>
        const username = "PENPALS";
        const password = "group1";
        // Get the modal
        const modal = document.getElementById("signupModal");
        // Get the button that opens the modal
        const signupBtn = document.getElementById("signupBtn");
        // Get the <span> element that closes the modal
        const closeModal = document.getElementById("closeModal");
        // When the user clicks the button, open the modal 
        signupBtn.onclick = function() {
            modal.style.display = "block";
        }
        // When the user clicks on <span> (x), close the modal
        closeModal.onclick = function() {
            modal.style.display = "none";
        }
        // When the user clicks anywhere outside of the modal, close it
        window.onclick = function(event) {
            if (event.target == modal) {
                modal.style.display = "none";
            }
        }
        // Handle the login form submission
        function checking_accesablilty() { // Correct function declaration
            const user_input_username = document.getElementById("username").value;
            const user_input_password = document.getElementById("password").value;
            // Check credentials
            if (user_input_username === username && user_input_password === password) {
                document.getElementById("status").innerHTML = "Access granted";
                statusElement.style.color = "#006400"
            } else {
                document.getElementById("status").innerHTML = "Access denied";
                statusElement.style.color = "red"
            }
        }
    </script>
</body>
 -->
