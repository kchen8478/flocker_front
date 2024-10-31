---
layout: post
title: LIMITLESS CONNECTIONS
#description: My Interests
hide: true
# menu: nav/home.html
---

<img src = "images/limitless connections.jpg">



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
