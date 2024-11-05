---
layout: post
title: GAMING
hide: true
---
<!-- OLD DASHBOARD -->
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Penpal Dashboard</title>
<style>
    /* body {
        font-family: Arial, sans-serif;
        display: flex;
        flex-direction: column;
        align-items: center;
        background-color: #f0f4f8;
        margin: 0;
        padding: 20px;
    } */
    .navbar {
        width: 100%;
        max-width: 1200px;
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
        max-width: 1200px;
        justify-content: space-between;
        gap: 20px;
    }
    .section {
        flex: 1;
        padding: 20px;
        background-color: white;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        border-radius: 8px;
        max-height: 400px;
        overflow-y: auto;
    }
    .section h2 {
        margin-top: 0;
        font-size: 1.8em;
        color: black;
    }
    .draft, .letter {
        border: 1px solid #ddd;
        padding: 10px;
        margin: 10px 0;
        border-radius: 4px;
        font-size: 1.1em;
        color: black;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }
    .draft span {
        flex-grow: 1;
        overflow: hidden;
        white-space: nowrap;
        text-overflow: ellipsis;
        margin-right: 10px; /* Add some space between text and delete button */
    }
    .delete-btn {
        background-color: #ff4d4d;
        border: none;
        color: white;
        padding: 4px 6px; /* Smaller padding for a smaller button */
        font-size: 0.8em; /* Smaller font size */
        cursor: pointer;
        border-radius: 4px;
        height: 28px; /* Standard button height */
        width: 28px; /* Standard button width */
    }
    .delete-btn:hover {
        background-color: #ff1a1a;
    }
    textarea {
        width: 100%;
        padding: 10px;
        font-size: 1.1em;
        height: 120px;
        resize: none;
        margin-top: 10px;
    }
    button {
        padding: 10px;
        width: 100%;
        font-size: 1.1em;
        cursor: pointer;
    }
</style>

<div class="navbar">
    <h1>Penpal Dashboard</h1>
    <button onclick="goHome()">Home</button>
    <button onclick="viewSavedDrafts()">Saved Drafts</button>
    <button onclick="chat()">Chatroom</button>
</div>

<div class="dashboard">
    <div class="section" id="roughDraftsSection">
        <h2>Rough Drafts</h2>
        <div id="drafts">
            <p>No drafts available.</p>
        </div>
        <textarea id="draftInput" placeholder="Write a rough draft..."></textarea>
        <button onclick="saveDraft()">Save Draft</button>
    </div>
    <div class="section" id="lettersReceivedSection">
        <h2>Letters Received</h2>
        <div id="letters">
            <!-- <div class="letter">Letter 1: Hello! Hope you're doing well!</div>
            <div class="letter">Letter 2: Looking forward to your reply!</div> -->
        </div>
    </div>
</div>

<script>
    let drafts = JSON.parse(localStorage.getItem("savedDrafts")) || [];

    function goHome() {
        window.location.href = "{{site.baseurl}}/"
    }

    function viewSavedDrafts() {
        const draftsDiv = document.getElementById("drafts");
        draftsDiv.innerHTML = '';

        if (drafts.length === 0) {
            draftsDiv.innerHTML = '<p>No saved drafts available.</p>';
            return;
        }

        drafts.forEach((draft, index) => {
            const draftElement = document.createElement("div");
            draftElement.className = "draft";
            draftElement.innerHTML = `
                <span>Saved Draft ${index + 1}: ${draft}</span>
                <button class="delete-btn" onclick="deleteDraft(${index})">X</button>
            `;
            draftsDiv.appendChild(draftElement);
        });
    }

    function saveDraft() {
        const draftInput = document.getElementById("draftInput").value;
        if (draftInput) {
            drafts.push(draftInput);
            localStorage.setItem("savedDrafts", JSON.stringify(drafts));
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
            draftElement.innerHTML = `
                <span>Draft ${index + 1}: ${draft}</span>
                <button class="delete-btn" onclick="deleteDraft(${index})">X</button>
            `;
            draftsDiv.appendChild(draftElement);
        });
    }

    function deleteDraft(index) {
        drafts.splice(index, 1);
        localStorage.setItem("savedDrafts", JSON.stringify(drafts));
        displayDrafts();
    }

    displayDrafts();
</script>
