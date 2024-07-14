# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 09:40:01 2024

@author: admin
"""

import tkinter as tk
from tkinter import messagebox
import random

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        global user_score
        user_score += 1
        return "You win!"
    else:
        global computer_score
        computer_score += 1
        return "Computer wins!"

# Function to handle user choice
def play_round(user_choice):
    computer_choice = random.choice(choices)
    result = determine_winner(user_choice, computer_choice)
    
    result_text.set(f"You chose: {user_choice}\nComputer chose: {computer_choice}\n{result}")
    score_text.set(f"User Score: {user_score}   Computer Score: {computer_score}")

    play_again = messagebox.askyesno("Play Again", "Do you want to play another round?")
    if not play_again:
        root.destroy()

# Initializing the main application window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

choices = ["Rock", "Paper", "Scissors"]
user_score = 0
computer_score = 0

# Result text
result_text = tk.StringVar()
result_text.set("Make your choice to start the game!")
score_text = tk.StringVar()
score_text.set(f"User Score: {user_score}   Computer Score: {computer_score}")

# Result label
result_label = tk.Label(root, textvariable=result_text, font=('Arial', 16), wraplength=300, justify="center")
result_label.pack(pady=10)

# Score label
score_label = tk.Label(root, textvariable=score_text, font=('Arial', 14))
score_label.pack(pady=5)

# Buttons for Rock, Paper, Scissors
for choice in choices:
    button = tk.Button(root, text=choice, font=('Arial', 18), command=lambda c=choice: play_round(c))
    button.pack(side=tk.LEFT, expand=True, padx=10, pady=10)

# Run the application
root.mainloop()
