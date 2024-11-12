---
layout: post
title: LIMITLESS CONNECTIONS
#description: My Interests
hide: true
# menu: nav/home.html
---
<img src = "images/limitless connections.jpg">

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
   <style>
       .container {
           display: flex;
           flex-wrap: wrap;
           justify-content: space-around;
           gap: 10px;
           padding: 5px;
           max-width: 1200px;
           margin: 0 auto;
       }
       /* Sections for each feature */
       .section {
           background-color: #282828;
           border-radius: 10px;
           padding: 20px;
           /* width: 210px; */
           width: 1500px;
           text-align: center;
           box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
       }
       .section h2 {
           color: #D64646;
           font-size: 1.5em;
           margin-bottom: 15px;
       }
       .section p {
           font-size: 0.9em;
           color: white;
           margin-bottom: 20px;
       }
       /* Stylish Buttons */
       .section button {
           background: linear-gradient(145deg, #589CDB, #DB5858);
           border: none;
           padding: 10px 20px;
           font-size: 1em;
           cursor: pointer;
           border-radius: 5px;
       }
       .section button:hover {
           background-color: #012A50;
           transform: scale(1.05);
       }
   </style>

   <div class="container">
       <div class="section">
           <h2>Chatroom</h2>
           <p>Make connections</p>
           <button onclick="location.href='{{site.baseurl}}/navigation/categories/overall'">Connect</button>
       </div>
</div>
<style>
    .post-form-container {
        border: 2px solid pink;
        border-radius: 8px;
        background-color: skyblue;
        padding: 15px;
        margin-top: 20px;
    }
    #roleSelect {
        width: 100%;
        padding: 10px;
        border: 2px solid pink;
        border-radius: 5px;
        margin-bottom: 10px;
    }
    #postInput {
        width: 100%;
        height: 100px;
        padding: 10px;
        border: 2px solid pink;
        border-radius: 5px;
        margin-bottom: 10px;
        resize: none;
    }
</style>
<!-- Post Submission Form -->
<div class="post-form-container">
    <h3>Add a New Post</h3>
    <form id="postForm">
        <select id="roleSelect" required>
            <option value="" disabled selected>Select your role</option>
            <option value="Student">Student</option>
            <option value="Admin">Admin</option>
        </select>
        <textarea id="postInput" placeholder="What's on your mind?" required></textarea>
        <button type="submit">Post</button>
    </form>
</div>

<script>
    function getReactions() {
        const reactions = localStorage.getItem('reactions');
        return reactions ? JSON.parse(reactions) : {};
    }

    function saveReactions(reactions) {
        localStorage.setItem('reactions', JSON.stringify(reactions));
    }

    function getPosts() {
        const posts = localStorage.getItem('posts');
        return posts ? JSON.parse(posts) : [];
    }

    function savePosts(posts) {
        localStorage.setItem('posts', JSON.stringify(posts));
    }

    document.addEventListener('DOMContentLoaded', () => {
        const reactions = getReactions();
        const posts = getPosts();

        // Load posts from localStorage
        posts.forEach(post => {
            createPostElement(post.username, post.content, post.id);
        });

        document.querySelectorAll('.post').forEach(postElement => {
            const postId = postElement.getAttribute('data-post-id');
            const postReactions = reactions[postId] || { thumbsUp: 0, heart: 0, fire: 0 };

            postElement.querySelector('.thumbsUp-count').textContent = postReactions.thumbsUp;
            postElement.querySelector('.heart-count').textContent = postReactions.heart;
            postElement.querySelector('.fire-count').textContent = postReactions.fire;
        });
    });

    function addReaction(postId, reactionType) {
        const reactions = getReactions();

        if (!reactions[postId]) {
            reactions[postId] = { thumbsUp: 0, heart: 0, fire: 0 };
        }

        reactions[postId][reactionType]++;
        saveReactions(reactions);

        const postElement = document.querySelector(`[data-post-id="${postId}"]`);
        const countElement = postElement.querySelector(`.${reactionType}-count`);
        countElement.textContent = reactions[postId][reactionType];
    }

    function createPostElement(username, content, postId) {
        // Create a new post element
        const newPost = document.createElement('div');
        newPost.className = 'post';
        newPost.setAttribute('data-post-id', postId);
        newPost.innerHTML = `
            <div class="post-header">
                <div class="post-icon"></div>
                <span class="post-username">${username}</span>
            </div>
            <p>${content}</p>
            <div class="reaction-icons">
                <span class="emoji" onclick="addReaction('${postId}', 'thumbsUp')">👍 <span class="thumbsUp-count">0</span></span>
                <span class="emoji" onclick="addReaction('${postId}', 'heart')">❤️ <span class="heart-count">0</span></span>
                <span class="emoji" onclick="addReaction('${postId}', 'fire')">🔥 <span class="fire-count">0</span></span>
            </div>
        `;

        // Append the new post to the posts wrapper
        document.getElementById('postsWrapper').prepend(newPost); // Add to the top
    }

    // Handle post submission
    document.getElementById('postForm').addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent page refresh

        const roleSelect = document.getElementById('roleSelect');
        const postInput = document.getElementById('postInput');
        const selectedRole = roleSelect.value; // Get selected role
        const newPostContent = postInput.value;

        // Create a unique ID based on timestamp
        const newPostId = Date.now();

        // Save the new post to localStorage
        const posts = getPosts();
        posts.push({ id: newPostId, username: selectedRole, content: newPostContent });
        savePosts(posts);

        // Create and display the new post
        createPostElement(selectedRole, newPostContent, newPostId);

        // Clear the input
        // Clear the input fields
        postInput.value = '';
        roleSelect.selectedIndex = 0; // Reset to default
    });

    // Handle message submission
    document.getElementById('messageForm').addEventListener('submit', function(event) {
        event.preventDefault();
        const messageInput = document.getElementById('messageInput');
        const messageContent = messageInput.value;

        // Create a new message element
        const newMessage = document.createElement('div');
        newMessage.textContent = messageContent;
        document.getElementById('chatArea').appendChild(newMessage);

        // Clear the input field
        messageInput.value = '';
    });
</script>