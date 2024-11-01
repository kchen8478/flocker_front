import tkinter as tk
import random

# List of prompts
prompts = [
    "What’s something you’re really passionate about, and how did you get into it?",
    "Do you have a favorite memory from school so far? I’d love to hear about it!",
    "What’s a skill or hobby you’d love to pick up if you had the time?",
    "Is there a class or subject that you find especially interesting? What do you like most about it?",
    "Who has been a big influence in your life? It could be anyone from family to a friend, or even someone you admire from afar.",
    "What’s one thing you want to achieve by the end of the school year?",
    "If you could describe your personality in just three words, what would they be?",
    "What’s something you’re proud of accomplishing, either this year or in the past?",
    "What’s one place you’ve always wanted to travel to, and why?",
    "If you could spend a day doing anything you love, what would your perfect day look like?"
]

# Select a random prompt
random_prompt = random.choice(prompts)

# Create the GUI window
root = tk.Tk()
root.title("Daily Prompt")
root.geometry("400x200")
root.resizable(False, False)

# Display the prompt at the top of the screen
prompt_label = tk.Label(root, text=random_prompt, wraplength=380, font=("Arial", 12), padx=10, pady=20)
prompt_label.pack(anchor="n")

# Run the application
root.mainloop()
