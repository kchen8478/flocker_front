---
layout: post
title: LIMITLESS CONNECTIONS
#description: My Interests
hide: true
# menu: nav/home.html
---
<img src = "images/limitless connections.jpg">

<div style="display: flex; justify-content: center; padding-top: 20px;">
  <div style="border: 2px solid #ddd; padding: 20px; border-radius: 12px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1); max-width: 600px; width: 100%; text-align: center;">
    <div style="display: flex; gap: 10px; justify-content: center;">
      <button onclick="redirectToPage('navigation/categories/sports')" style="background-color: #1e90ff; color: white; padding: 10px 20px; font-size: 16px; font-weight: bold; border: none; border-radius: 8px; cursor: pointer; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); transition: transform 0.2s;">
        Sports
      </button>
      <button onclick="redirectToPage('navigation/categories/music')" style="background-color: #32cd32; color: white; padding: 10px 20px; font-size: 16px; font-weight: bold; border: none; border-radius: 8px; cursor: pointer; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); transition: transform 0.2s;">
        Music
      </button>
      <button onclick="redirectToPage('navigation/categories/movies')" style="background-color: #ff4500; color: white; padding: 10px 20px; font-size: 16px; font-weight: bold; border: none; border-radius: 8px; cursor: pointer; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); transition: transform 0.2s;">
        Movies
      </button>
      <button onclick="redirectToPage('navigation/categories/gaming')" style="background-color: #9370db; color: white; padding: 10px 20px; font-size: 16px; font-weight: bold; border: none; border-radius: 8px; cursor: pointer; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); transition: transform 0.2s;">
        Gaming
      </button>
    </div>
  </div>
</div>


<script>
  function redirectToPage(url) {
    window.location.href = url;
  }
</script>
