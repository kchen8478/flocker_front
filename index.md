---
layout: post
title: My Space 
description: My Interests
hide: true
menu: nav/home.html
---


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


<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Text Platform</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .text-platform {
            width: 300px;
            text-align: center;
        }
        textarea {
            width: 100%;
            height: 100px;
            margin-bottom: 10px;
            padding: 10px;
            font-size: 16px;
            resize: none;
        }
        button {
            width: 100%;
            padding: 10px;
            font-size: 16px;
            cursor: pointer;
        }
        .output {
            margin-top: 20px;
            font-weight: bold;
            color: #333;
        }
    </style>
</head>
<body>

<div class="text-platform">
    <h2>Text Platform</h2>
    <textarea id="textInput" placeholder="Type your message here..."></textarea>
    <button onclick="sendMessage()">Send</button>
    <div id="output" class="output"></div>
</div>

<script>
    function sendMessage() {
        const textInput = document.getElementById("textInput").value;
        const output = document.getElementById("output");
        output.innerText = `Message sent: ${textInput}`;
    }
</script>
</body>
</html>


<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Penpal Dashboard</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            background-color: #f0f4f8;
            margin: 0;
            padding: 20px;
        }
        .navbar {
            width: 100%;
            max-width: 800px;
            display: flex;
            justify-content: space-between;
            margin-bottom: 20px;
            background-color: #333;
            padding: 10px 20px;
            color: white;
        }
        .navbar h1 {
            margin: 0;
        }
        .navbar button {
            padding: 10px;
            font-size: 16px;
            background-color: #666;
            border: none;
            color: white;
            cursor: pointer;
        }
        .navbar button:hover {
            background-color: #444;
        }
        .dashboard {
            display: flex;
            width: 100%;
            max-width: 800px;
            justify-content: space-between;
            gap: 20px;
        }
        .section {
            flex: 1;
            padding: 20px;
            background-color: white;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            border-radius: 8px;
        }
        .section h2 {
            margin-top: 0;
            font-size: 1.5em;
        }
        .draft, .letter {
            border: 1px solid #ddd;
            padding: 10px;
            margin: 10px 0;
            border-radius: 4px;
        }
    </style>
</head>
<body>

<div class="navbar">
    <h1>Penpal Dashboard</h1>
    <button onclick="goHome()">Home</button>
</div>

<div class="dashboard">
    <div class="section" id="roughDraftsSection">
        <h2 >Rough Drafts</h2>
        <div id="drafts">
            <p>No drafts available.</p>
        </div>
        <textarea id="draftInput" placeholder="Write a rough draft..."></textarea>
        <button onclick="saveDraft()">Save Draft</button>
    </div>
    <div class="section" id="lettersReceivedSection">
        <h2 color = "black" >Letters Received</h2>
        <div id="letters">
            <p>No letters received yet.</p>
        </div>
    </div>
</div>

<script>
    let drafts = [];
    let lettersReceived = ["Hello! Hope you're doing well!", "Looking forward to your reply!"];

    function goHome() {
        alert("Going back to home...");
        // Add code to navigate to the home page.
    }

    function saveDraft() {
        const draftInput = document.getElementById("draftInput").value;
        if (draftInput) {
            drafts.push(draftInput);
            document.getElementById("draftInput").value = '';
            displayDrafts();
        } else {
            alert("Draft cannot be empty!");
        }
    }

    function displayDrafts() {
        const draftsDiv = document.getElementById("drafts");
        draftsDiv.innerHTML = '';
        drafts.forEach((draft, index) => {
            const draftElement = document.createElement("div");
            draftElement.className = "draft";
            draftElement.innerText = `Draft ${index + 1}: ${draft}`;
            draftsDiv.appendChild(draftElement);
        });
    }

    function displayLetters() {
        const lettersDiv = document.getElementById("letters");
        lettersDiv.innerHTML = '';
        lettersReceived.forEach((letter, index) => {
            const letterElement = document.createElement("div");
            letterElement.className = "letter";
            letterElement.innerText = `Letter ${index + 1}: ${letter}`;
            lettersDiv.appendChild(letterElement);
        });
    }

    // Initial display
    displayDrafts();
    displayLetters();
</script>

</body>
</html>

