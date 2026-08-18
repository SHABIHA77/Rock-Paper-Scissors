import tkinter as tk
from tkinter import messagebox
import random
import os
import winsound


# =========================================================
# GAME DATA
# =========================================================

CHOICES = ["Rock", "Paper", "Scissors"]

player_score = 0
computer_score = 0
draw_score = 0

feedbacks = []

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SOUND_DIR = os.path.join(BASE_DIR, "sounds")


# =========================================================
# SOUND
# =========================================================

def play_sound(filename):

    sound_path = os.path.join(SOUND_DIR, filename)

    if os.path.exists(sound_path):

        try:
            winsound.PlaySound(
                sound_path,
                winsound.SND_FILENAME | winsound.SND_ASYNC
            )
        except Exception:
            pass


# =========================================================
# RESULT POPUP
# =========================================================

def show_result_popup(result, player_choice, computer_choice):

    popup = tk.Toplevel(root)

    popup.title("Game Result")
    popup.geometry("500x400")
    popup.resizable(False, False)
    popup.configure(bg="#F4F4F4")

    popup.transient(root)
    popup.grab_set()

    if result == "win":

        title = "YOU WIN! 🎉"
        title_color = "#1B8A3A"
        sound = "Win.mp3"

    elif result == "lose":

        title = "YOU LOSE! 😢"
        title_color = "#C62828"
        sound = "Lose.mp3"

    else:

        title = "IT'S A DRAW! 🤝"
        title_color = "#D68910"
        sound = "Draw.mp3"

    play_sound(sound)

    tk.Label(
        popup,
        text=title,
        font=("Arial", 30, "bold"),
        bg="#F4F4F4",
        fg=title_color
    ).pack(pady=(50, 25))

    tk.Label(
        popup,
        text=f"You chose: {player_choice}",
        font=("Arial", 15),
        bg="#F4F4F4",
        fg="#333333"
    ).pack(pady=5)

    tk.Label(
        popup,
        text=f"Computer chose: {computer_choice}",
        font=("Arial", 15),
        bg="#F4F4F4",
        fg="#333333"
    ).pack(pady=5)

    tk.Button(
        popup,
        text="OK",
        font=("Arial", 12, "bold"),
        width=15,
        height=2,
        command=popup.destroy
    ).pack(pady=30)


# =========================================================
# PLAY GAME
# =========================================================

def play_game(player_choice):

    global player_score
    global computer_score
    global draw_score

    play_sound("Click.mp3")

    computer_choice = random.choice(CHOICES)

    if player_choice == computer_choice:

        draw_score += 1
        result = "draw"

    elif (
        (player_choice == "Rock" and computer_choice == "Scissors")
        or
        (player_choice == "Paper" and computer_choice == "Rock")
        or
        (player_choice == "Scissors" and computer_choice == "Paper")
    ):

        player_score += 1
        result = "win"

    else:

        computer_score += 1
        result = "lose"

    update_score()

    show_result_popup(
        result,
        player_choice,
        computer_choice
    )


# =========================================================
# UPDATE SCORE
# =========================================================

def update_score():

    score_label.config(
        text=(
            f"YOU: {player_score}     "
            f"COMPUTER: {computer_score}     "
            f"DRAW: {draw_score}"
        )
    )


# =========================================================
# RESET GAME
# =========================================================

def reset_game():

    global player_score
    global computer_score
    global draw_score

    player_score = 0
    computer_score = 0
    draw_score = 0

    update_score()

    play_sound("Click.mp3")


# =========================================================
# EXIT
# =========================================================

def exit_game():

    answer = messagebox.askyesno(
        "Exit Game",
        "Are you sure you want to exit?"
    )

    if answer:
        root.destroy()


# =========================================================
# GIVE FEEDBACK
# =========================================================

def give_feedback():

    feedback_window = tk.Toplevel(root)

    feedback_window.title("Give Feedback")
    feedback_window.geometry("550x520")
    feedback_window.resizable(False, False)
    feedback_window.configure(bg="#F4F4F4")

    feedback_window.transient(root)

    # -----------------------------------------------------
    # TITLE
    # -----------------------------------------------------

    tk.Label(
        feedback_window,
        text="GIVE YOUR FEEDBACK",
        font=("Arial", 24, "bold"),
        bg="#F4F4F4",
        fg="#222222"
    ).pack(pady=(30, 5))

    tk.Label(
        feedback_window,
        text="We would love to hear your thoughts!",
        font=("Arial", 12),
        bg="#F4F4F4",
        fg="#666666"
    ).pack(pady=5)

    # -----------------------------------------------------
    # RATING
    # -----------------------------------------------------

    tk.Label(
        feedback_window,
        text="Your Rating",
        font=("Arial", 14, "bold"),
        bg="#F4F4F4",
        fg="#333333"
    ).pack(pady=(30, 8))

    selected_rating = tk.IntVar(
        value=5
    )

    rating_frame = tk.Frame(
        feedback_window,
        bg="#F4F4F4"
    )

    rating_frame.pack()

    rating_buttons = []

    def select_rating(rating):

        selected_rating.set(rating)

        for i, button in enumerate(
            rating_buttons,
            start=1
        ):

            if i <= rating:
                button.config(text="★")
            else:
                button.config(text="☆")

    for i in range(1, 6):

        button = tk.Button(
            rating_frame,
            text="★",
            font=("Arial", 25),
            relief="flat",
            bg="#F4F4F4",
            fg="#D68910",
            command=lambda r=i: select_rating(r)
        )

        button.pack(
            side="left",
            padx=3
        )

        rating_buttons.append(button)

    # -----------------------------------------------------
    # FEEDBACK TEXT
    # -----------------------------------------------------

    tk.Label(
        feedback_window,
        text="Your Feedback",
        font=("Arial", 14, "bold"),
        bg="#F4F4F4",
        fg="#333333"
    ).pack(
        anchor="w",
        padx=65,
        pady=(30, 8)
    )

    feedback_box = tk.Text(
        feedback_window,
        width=48,
        height=8,
        font=("Arial", 11)
    )

    feedback_box.pack()

    # -----------------------------------------------------
    # SUBMIT
    # -----------------------------------------------------

    def submit_feedback():

        text = feedback_box.get(
            "1.0",
            tk.END
        ).strip()

        if text == "":

            messagebox.showwarning(
                "Feedback",
                "Please write your feedback.",
                parent=feedback_window
            )

            return

        new_feedback = {
            "rating": selected_rating.get(),
            "text": text
        }

        feedbacks.append(
            new_feedback
        )

        messagebox.showinfo(
            "Thank You",
            "Your feedback has been submitted successfully! ❤️",
            parent=feedback_window
        )

        feedback_window.destroy()

    tk.Button(
        feedback_window,
        text="SUBMIT FEEDBACK",
        font=("Arial", 12, "bold"),
        width=24,
        height=2,
        command=submit_feedback
    ).pack(
        pady=25
    )


# =========================================================
# VIEW FEEDBACK
# =========================================================

def view_feedback():

    feedback_window = tk.Toplevel(root)

    feedback_window.title("View Feedback")
    feedback_window.geometry("700x620")
    feedback_window.resizable(False, False)
    feedback_window.configure(bg="#F4F4F4")

    # -----------------------------------------------------
    # TITLE
    # -----------------------------------------------------

    tk.Label(
        feedback_window,
        text="ALL FEEDBACK",
        font=("Arial", 24, "bold"),
        bg="#F4F4F4",
        fg="#222222"
    ).pack(
        pady=(25, 5)
    )

    tk.Label(
        feedback_window,
        text="What players are saying",
        font=("Arial", 12),
        bg="#F4F4F4",
        fg="#666666"
    ).pack(
        pady=5
    )

    # -----------------------------------------------------
    # NO FEEDBACK
    # -----------------------------------------------------

    if len(feedbacks) == 0:

        tk.Label(
            feedback_window,
            text="No feedback submitted yet.",
            font=("Arial", 14),
            bg="#F4F4F4",
            fg="#666666"
        ).pack(
            pady=80
        )

        return

    # -----------------------------------------------------
    # SCROLL AREA
    # -----------------------------------------------------

    canvas = tk.Canvas(
        feedback_window,
        bg="#F4F4F4",
        highlightthickness=0
    )

    scrollbar = tk.Scrollbar(
        feedback_window,
        orient="vertical",
        command=canvas.yview
    )

    scroll_frame = tk.Frame(
        canvas,
        bg="#F4F4F4"
    )

    scroll_frame.bind(
        "<Configure>",
        lambda event: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window(
        (0, 0),
        window=scroll_frame,
        anchor="nw",
        width=660
    )

    canvas.configure(
        yscrollcommand=scrollbar.set
    )

    canvas.pack(
        side="left",
        fill="both",
        expand=True,
        padx=(20, 0),
        pady=15
    )

    scrollbar.pack(
        side="right",
        fill="y",
        pady=15
    )

    # -----------------------------------------------------
    # FEEDBACK CARDS
    # -----------------------------------------------------

    for feedback in feedbacks:

        card = tk.Frame(
            scroll_frame,
            bg="white",
            bd=1,
            relief="solid"
        )

        card.pack(
            fill="x",
            padx=10,
            pady=8
        )

        # Stars

        stars = (
            "★" * feedback["rating"]
            +
            "☆" * (5 - feedback["rating"])
        )

        tk.Label(
            card,
            text=stars,
            font=("Arial", 22, "bold"),
            fg="#D68910",
            bg="white"
        ).pack(
            anchor="w",
            padx=18,
            pady=(15, 8)
        )

        # Feedback text

        tk.Label(
            card,
            text=f'“{feedback["text"]}”',
            font=("Arial", 13),
            bg="white",
            fg="#333333",
            wraplength=600,
            justify="left"
        ).pack(
            anchor="w",
            padx=18,
            pady=(5, 15)
        )


# =========================================================
# MAIN WINDOW
# =========================================================

root = tk.Tk()

root.title(
    "Rock Paper Scissors"
)

root.geometry(
    "900x720"
)

root.resizable(
    False,
    False
)

root.configure(
    bg="#F4F4F4"
)


# =========================================================
# TITLE
# =========================================================

tk.Label(
    root,
    text="ROCK PAPER SCISSORS",
    font=("Arial", 32, "bold"),
    bg="#F4F4F4",
    fg="#222222"
).pack(
    pady=(30, 5)
)

tk.Label(
    root,
    text="Choose your move!",
    font=("Arial", 14),
    bg="#F4F4F4",
    fg="#666666"
).pack(
    pady=5
)


# =========================================================
# SCORE
# =========================================================

score_label = tk.Label(
    root,
    text="YOU: 0     COMPUTER: 0     DRAW: 0",
    font=("Arial", 17, "bold"),
    bg="white",
    fg="#222222",
    padx=25,
    pady=18
)

score_label.pack(
    pady=20
)


# =========================================================
# GAME BUTTONS
# =========================================================

button_frame = tk.Frame(
    root,
    bg="#F4F4F4"
)

button_frame.pack(
    pady=20
)


tk.Button(
    button_frame,
    text="🪨 ROCK",
    font=("Arial", 15, "bold"),
    width=15,
    height=3,
    command=lambda: play_game("Rock")
).grid(
    row=0,
    column=0,
    padx=10
)


tk.Button(
    button_frame,
    text="📄 PAPER",
    font=("Arial", 15, "bold"),
    width=15,
    height=3,
    command=lambda: play_game("Paper")
).grid(
    row=0,
    column=1,
    padx=10
)


tk.Button(
    button_frame,
    text="✂ SCISSORS",
    font=("Arial", 15, "bold"),
    width=15,
    height=3,
    command=lambda: play_game("Scissors")
).grid(
    row=0,
    column=2,
    padx=10
)


# =========================================================
# RESET + EXIT
# =========================================================

control_frame = tk.Frame(
    root,
    bg="#F4F4F4"
)

control_frame.pack(
    pady=20
)


tk.Button(
    control_frame,
    text="RESET GAME",
    font=("Arial", 11, "bold"),
    width=18,
    height=2,
    command=reset_game
).grid(
    row=0,
    column=0,
    padx=10
)


tk.Button(
    control_frame,
    text="EXIT",
    font=("Arial", 11, "bold"),
    width=18,
    height=2,
    command=exit_game
).grid(
    row=0,
    column=1,
    padx=10
)


# =========================================================
# FEEDBACK BUTTONS
# =========================================================

feedback_frame = tk.Frame(
    root,
    bg="#F4F4F4"
)

feedback_frame.pack(
    pady=10
)


tk.Button(
    feedback_frame,
    text="GIVE FEEDBACK",
    font=("Arial", 11, "bold"),
    width=20,
    height=2,
    command=give_feedback
).grid(
    row=0,
    column=0,
    padx=8
)


tk.Button(
    feedback_frame,
    text="VIEW FEEDBACK",
    font=("Arial", 11, "bold"),
    width=20,
    height=2,
    command=view_feedback
).grid(
    row=0,
    column=1,
    padx=8
)


# =========================================================
# START APPLICATION
# =========================================================

root.mainloop()