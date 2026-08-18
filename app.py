import tkinter as tk
from tkinter import messagebox
import random
import os
import winsound


# =========================
# GAME VARIABLES
# =========================

choices = ["Rock", "Paper", "Scissors"]

player_score = 0
computer_score = 0
draw_score = 0

feedbacks = []

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SOUND_DIR = os.path.join(BASE_DIR, "sounds")


# =========================
# SOUND
# =========================

def play_sound(filename):
    sound_path = os.path.join(SOUND_DIR, filename)

    if os.path.exists(sound_path):
        try:
            winsound.PlaySound(
                sound_path,
                winsound.SND_FILENAME | winsound.SND_ASYNC
            )
        except:
            pass


# =========================
# PLAY GAME
# =========================

def play_game(player_choice):

    global player_score, computer_score, draw_score

    play_sound("Click.mp3")

    computer_choice = random.choice(choices)

    player_choice_label.config(
        text=f"You chose: {player_choice}"
    )

    computer_choice_label.config(
        text=f"Computer chose: {computer_choice}"
    )

    if player_choice == computer_choice:

        draw_score += 1

        result_label.config(
            text="IT'S A DRAW! 🤝"
        )

        play_sound("Draw.mp3")

    elif (
        (player_choice == "Rock" and computer_choice == "Scissors")
        or
        (player_choice == "Paper" and computer_choice == "Rock")
        or
        (player_choice == "Scissors" and computer_choice == "Paper")
    ):

        player_score += 1

        result_label.config(
            text="YOU WIN! 🎉"
        )

        play_sound("Win.mp3")

    else:

        computer_score += 1

        result_label.config(
            text="YOU LOSE! 😢"
        )

        play_sound("Lose.mp3")

    update_score()


# =========================
# UPDATE SCORE
# =========================

def update_score():

    score_label.config(
        text=(
            f"YOU: {player_score}     "
            f"COMPUTER: {computer_score}     "
            f"DRAW: {draw_score}"
        )
    )


# =========================
# RESET GAME
# =========================

def reset_game():

    global player_score, computer_score, draw_score

    player_score = 0
    computer_score = 0
    draw_score = 0

    player_choice_label.config(
        text="You chose: -"
    )

    computer_choice_label.config(
        text="Computer chose: -"
    )

    result_label.config(
        text="MAKE YOUR CHOICE!"
    )

    update_score()

    play_sound("Click.mp3")


# =========================
# EXIT
# =========================

def exit_game():

    answer = messagebox.askyesno(
        "Exit Game",
        "Are you sure you want to exit?"
    )

    if answer:
        root.destroy()


# =========================
# GIVE FEEDBACK
# =========================

def open_feedback():

    feedback_window = tk.Toplevel(root)

    feedback_window.title("Give Feedback")
    feedback_window.geometry("500x400")
    feedback_window.resizable(False, False)
    feedback_window.configure(bg="#F4F4F4")

    title = tk.Label(
        feedback_window,
        text="GIVE YOUR FEEDBACK",
        font=("Arial", 20, "bold"),
        bg="#F4F4F4",
        fg="#222222"
    )

    title.pack(pady=(30, 15))

    instruction = tk.Label(
        feedback_window,
        text="Tell us what you think about the game:",
        font=("Arial", 12),
        bg="#F4F4F4",
        fg="#555555"
    )

    instruction.pack()

    feedback_box = tk.Text(
        feedback_window,
        width=50,
        height=8,
        font=("Arial", 11)
    )

    feedback_box.pack(pady=15)

    def submit_feedback():

        feedback = feedback_box.get(
            "1.0",
            tk.END
        ).strip()

        if feedback == "":
            messagebox.showwarning(
                "Feedback",
                "Please write your feedback first.",
                parent=feedback_window
            )
            return

        feedbacks.append(feedback)

        feedback_box.delete(
            "1.0",
            tk.END
        )

        messagebox.showinfo(
            "Thank You",
            "Your feedback has been submitted successfully! ❤️",
            parent=feedback_window
        )

        feedback_window.destroy()

        view_feedback_button.pack(pady=8)

    submit_button = tk.Button(
        feedback_window,
        text="SUBMIT FEEDBACK",
        font=("Arial", 12, "bold"),
        width=20,
        height=2,
        command=submit_feedback
    )

    submit_button.pack()


# =========================
# VIEW FEEDBACK
# =========================

def view_feedback():

    feedback_window = tk.Toplevel(root)

    feedback_window.title("View Feedback")
    feedback_window.geometry("600x500")
    feedback_window.resizable(False, False)
    feedback_window.configure(bg="#F4F4F4")

    title = tk.Label(
        feedback_window,
        text="ALL FEEDBACK",
        font=("Arial", 22, "bold"),
        bg="#F4F4F4",
        fg="#222222"
    )

    title.pack(pady=(25, 15))

    if len(feedbacks) == 0:

        empty_label = tk.Label(
            feedback_window,
            text="No feedback submitted yet.",
            font=("Arial", 13),
            bg="#F4F4F4",
            fg="#666666"
        )

        empty_label.pack(pady=40)

        return

    feedback_list = tk.Listbox(
        feedback_window,
        width=65,
        height=18,
        font=("Arial", 11)
    )

    feedback_list.pack(
        padx=20,
        pady=10
    )

    for number, feedback in enumerate(feedbacks, start=1):

        feedback_list.insert(
            tk.END,
            f"{number}. {feedback}"
        )


# =========================
# MAIN WINDOW
# =========================

root = tk.Tk()

root.title("Rock Paper Scissors")
root.geometry("850x700")
root.resizable(False, False)
root.configure(bg="#F4F4F4")


# =========================
# TITLE
# =========================

title_label = tk.Label(
    root,
    text="ROCK PAPER SCISSORS",
    font=("Arial", 30, "bold"),
    bg="#F4F4F4",
    fg="#222222"
)

title_label.pack(pady=(25, 5))


subtitle_label = tk.Label(
    root,
    text="Choose your move!",
    font=("Arial", 14),
    bg="#F4F4F4",
    fg="#666666"
)

subtitle_label.pack()


# =========================
# SCORE
# =========================

score_label = tk.Label(
    root,
    text="YOU: 0     COMPUTER: 0     DRAW: 0",
    font=("Arial", 17, "bold"),
    bg="white",
    fg="#222222",
    padx=25,
    pady=15
)

score_label.pack(pady=15)


# =========================
# CHOICE
# =========================

player_choice_label = tk.Label(
    root,
    text="You chose: -",
    font=("Arial", 14),
    bg="#F4F4F4"
)

player_choice_label.pack(pady=4)


computer_choice_label = tk.Label(
    root,
    text="Computer chose: -",
    font=("Arial", 14),
    bg="#F4F4F4"
)

computer_choice_label.pack(pady=4)


# =========================
# RESULT
# =========================

result_label = tk.Label(
    root,
    text="MAKE YOUR CHOICE!",
    font=("Arial", 25, "bold"),
    bg="#F4F4F4",
    fg="#222222"
)

result_label.pack(pady=18)


# =========================
# GAME BUTTONS
# =========================

button_frame = tk.Frame(
    root,
    bg="#F4F4F4"
)

button_frame.pack(pady=10)


rock_button = tk.Button(
    button_frame,
    text="🪨 ROCK",
    font=("Arial", 15, "bold"),
    width=15,
    height=2,
    command=lambda: play_game("Rock")
)

rock_button.grid(
    row=0,
    column=0,
    padx=8
)


paper_button = tk.Button(
    button_frame,
    text="📄 PAPER",
    font=("Arial", 15, "bold"),
    width=15,
    height=2,
    command=lambda: play_game("Paper")
)

paper_button.grid(
    row=0,
    column=1,
    padx=8
)


scissors_button = tk.Button(
    button_frame,
    text="✂ SCISSORS",
    font=("Arial", 15, "bold"),
    width=15,
    height=2,
    command=lambda: play_game("Scissors")
)

scissors_button.grid(
    row=0,
    column=2,
    padx=8
)


# =========================
# RESET & EXIT
# =========================

control_frame = tk.Frame(
    root,
    bg="#F4F4F4"
)

control_frame.pack(pady=15)


reset_button = tk.Button(
    control_frame,
    text="RESET GAME",
    font=("Arial", 11, "bold"),
    width=15,
    command=reset_game
)

reset_button.grid(
    row=0,
    column=0,
    padx=10
)


exit_button = tk.Button(
    control_frame,
    text="EXIT",
    font=("Arial", 11, "bold"),
    width=15,
    command=exit_game
)

exit_button.grid(
    row=0,
    column=1,
    padx=10
)


# =========================
# FEEDBACK BUTTON
# =========================

feedback_button = tk.Button(
    root,
    text="GIVE FEEDBACK",
    font=("Arial", 12, "bold"),
    width=22,
    height=2,
    command=open_feedback
)

feedback_button.pack(pady=8)


# =========================
# VIEW FEEDBACK BUTTON
# =========================

view_feedback_button = tk.Button(
    root,
    text="VIEW FEEDBACK",
    font=("Arial", 12, "bold"),
    width=22,
    height=2,
    command=view_feedback
)

# Initially hidden
# It appears after feedback is submitted.


# =========================
# START
# =========================

root.mainloop()