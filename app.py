import tkinter as tk
from tkinter import messagebox
import random

# Game variables
player_score = 0
computer_score = 0
draw_score = 0

choices = ["Rock", "Paper", "Scissors"]


# -------------------------
# Game Function
# -------------------------

def play_game(player_choice):
    global player_score, computer_score, draw_score

    computer_choice = random.choice(choices)

    player_choice_label.config(
        text=f"You chose: {player_choice}"
    )

    computer_choice_label.config(
        text=f"Computer chose: {computer_choice}"
    )

    if player_choice == computer_choice:
        result = "It's a Draw! 🤝"
        draw_score += 1

    elif (
        (player_choice == "Rock" and computer_choice == "Scissors")
        or
        (player_choice == "Paper" and computer_choice == "Rock")
        or
        (player_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You Win! 🎉"
        player_score += 1

    else:
        result = "You Lose! 😢"
        computer_score += 1

    result_label.config(text=result)

    score_label.config(
        text=f"You: {player_score}    "
             f"Computer: {computer_score}    "
             f"Draw: {draw_score}"
    )


# -------------------------
# Reset Function
# -------------------------

def reset_game():
    global player_score, computer_score, draw_score

    player_score = 0
    computer_score = 0
    draw_score = 0

    player_choice_label.config(text="You chose: -")
    computer_choice_label.config(text="Computer chose: -")
    result_label.config(text="Make your choice!")

    score_label.config(
        text="You: 0    Computer: 0    Draw: 0"
    )


# -------------------------
# Exit Function
# -------------------------

def exit_game():
    answer = messagebox.askyesno(
        "Exit Game",
        "Are you sure you want to exit?"
    )

    if answer:
        root.destroy()


# -------------------------
# Main Window
# -------------------------

root = tk.Tk()

root.title("Rock Paper Scissors")
root.geometry("800x650")
root.resizable(False, False)

root.configure(bg="#f4f4f4")


# -------------------------
# Title
# -------------------------

title_label = tk.Label(
    root,
    text="ROCK PAPER SCISSORS",
    font=("Arial", 28, "bold"),
    bg="#f4f4f4",
    fg="#222222"
)

title_label.pack(pady=(30, 5))


subtitle_label = tk.Label(
    root,
    text="Choose your move!",
    font=("Arial", 14),
    bg="#f4f4f4",
    fg="#666666"
)

subtitle_label.pack(pady=5)


# -------------------------
# Score
# -------------------------

score_label = tk.Label(
    root,
    text="You: 0    Computer: 0    Draw: 0",
    font=("Arial", 16, "bold"),
    bg="white",
    fg="#222222",
    padx=20,
    pady=15
)

score_label.pack(pady=20)


# -------------------------
# Choices
# -------------------------

player_choice_label = tk.Label(
    root,
    text="You chose: -",
    font=("Arial", 14),
    bg="#f4f4f4"
)

player_choice_label.pack(pady=5)


computer_choice_label = tk.Label(
    root,
    text="Computer chose: -",
    font=("Arial", 14),
    bg="#f4f4f4"
)

computer_choice_label.pack(pady=5)


# -------------------------
# Result
# -------------------------

result_label = tk.Label(
    root,
    text="Make your choice!",
    font=("Arial", 24, "bold"),
    bg="#f4f4f4",
    fg="#222222"
)

result_label.pack(pady=20)


# -------------------------
# Game Buttons
# -------------------------

button_frame = tk.Frame(
    root,
    bg="#f4f4f4"
)

button_frame.pack(pady=10)


rock_button = tk.Button(
    button_frame,
    text="🪨 ROCK",
    font=("Arial", 14, "bold"),
    width=14,
    height=2,
    command=lambda: play_game("Rock")
)

rock_button.grid(row=0, column=0, padx=8)


paper_button = tk.Button(
    button_frame,
    text="📄 PAPER",
    font=("Arial", 14, "bold"),
    width=14,
    height=2,
    command=lambda: play_game("Paper")
)

paper_button.grid(row=0, column=1, padx=8)


scissors_button = tk.Button(
    button_frame,
    text="✂ SCISSORS",
    font=("Arial", 14, "bold"),
    width=14,
    height=2,
    command=lambda: play_game("Scissors")
)

scissors_button.grid(row=0, column=2, padx=8)


# -------------------------
# Control Buttons
# -------------------------

control_frame = tk.Frame(
    root,
    bg="#f4f4f4"
)

control_frame.pack(pady=20)


reset_button = tk.Button(
    control_frame,
    text="RESET GAME",
    font=("Arial", 11, "bold"),
    width=15,
    command=reset_game
)

reset_button.grid(row=0, column=0, padx=10)


exit_button = tk.Button(
    control_frame,
    text="EXIT",
    font=("Arial", 11, "bold"),
    width=15,
    command=exit_game
)

exit_button.grid(row=0, column=1, padx=10)


# -------------------------
# Start Game
# -------------------------

root.mainloop()