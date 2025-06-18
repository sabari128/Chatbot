import tkinter as tk
from tkinter import Scrollbar
import random

# Bot responses dictionary
bot_responses = {
    "hi": ["Hey there! 👋", "Hello human!", "Yo! What's cookin'?"],
    "hello": ["Hiya!", "Hellooo!", "Vanakam...! 😎"],
    "name": ["I'm ChatBunny 🐰", "Call me whatever you want 😅",  " 🤖"],
    "how are you": ["Feeling' electric ⚡", "Charged up and chillin'!"],
    "what is python": [" A python is an type of snake which larger in size 😅🐍"],
    "whatsup":["Nothing to sayy"],
    "whats the time":["Go and see the clock..buddy"],
    "bye": ["That's great😅","Catch ya later! 👋", "Peace out! ✌️", "Logging off... beep beep! 📴"],
    "joke": [
        "Why don't robots panic? Because they have nerves of steel! 😂",
        "I would tell you a UDP joke... but you might not get it. 😜",
        "Why did the Python go to therapy? Too many 'if' issues! 🐍",
        "The laptop are around with ants...because it has cookies 😂"
    ],
    "default": ["Hmm... I didn't get that 🤔", "Say what? 😅", "Type correctly, buddy!"]
}

# Function to get bot response
def get_bot_reply(user_input):
    user_input = user_input.lower()
    for key in bot_responses:
        if key in user_input:
            return random.choice(bot_responses[key])
    return random.choice(bot_responses["default"])

# Send message
def send_message(event=None):
    user_msg = user_entry.get().strip()
    if user_msg == "":
        return

    display_message("You", user_msg, "lightgreen", "e")
    user_entry.delete(0, tk.END)
    
    bot_reply = get_bot_reply(user_msg)
    display_message("Bot", bot_reply, "lavender", "w")

# Display message bubble
def display_message(sender, msg, color, side):
    msg_frame = tk.Frame(chat_frame, bg="#f0f0f0")
    msg_bubble = tk.Label(
        msg_frame,
        text=f"{sender}: {msg}",
        bg=color,
        wraplength=300,
        justify="center",
        font=("Times New Roman", 11),
        padx=10,
        pady=6,
        bd=0,
        anchor=side
    )
    msg_bubble.pack(anchor=side)
    msg_frame.pack(anchor=side, pady=2, padx=10, fill="x")
    
    # Scroll to the bottom
    canvas.update_idletasks()
    canvas.yview_moveto(1.0)

# Main Window
root = tk.Tk()
root.title("🤖 ChatBunny - Chatbot")
root.geometry("480x600")
root.configure(bg="#f0f0f0")

# Canvas and Scrollbar for Chat Area
chat_frame_container = tk.Frame(root, bg="#f0f0f0")
chat_frame_container.pack(fill=tk.BOTH, expand=True)

canvas = tk.Canvas(chat_frame_container, bg="#f0f0f0", highlightthickness=0)
scrollbar = Scrollbar(chat_frame_container, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)

scrollable_frame = tk.Frame(canvas, bg="#f0f0f0")
scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

chat_frame = scrollable_frame

# User Input Area
user_input_frame = tk.Frame(root, bg="#f0f0f0")
user_input_frame.pack(fill=tk.X, side=tk.BOTTOM)

user_entry = tk.Entry(user_input_frame, font=("Arial", 13))
user_entry.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
user_entry.bind("<Return>", send_message)

send_btn = tk.Button(user_input_frame, text="Send", bg="#4CAF50", fg="white", font=("Arial", 11), command=send_message)
send_btn.pack(side=tk.RIGHT, padx=10, pady=10)

# Welcome Message
display_message("Bot", "Hey there! I'm ChatBunny 🐰. Say the stuffs...!", "lavender", "w")

root.mainloop()
