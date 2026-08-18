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


# =========================================================
# PATHS
# =========================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SOUND_DIR = os.path.join(BASE_DIR, "sounds")


# =========================================================
# COLORS
# =========================================================

BG_COLOR = "#030712"

GLASS = "#091525"
GLASS_2 = "#0D1D30"

NEON_BLUE = "#00D9FF"
NEON_CYAN = "#19F5FF"
NEON_PURPLE = "#A855F7"
NEON_GOLD = "#FFD21F"

WHITE = "#FFFFFF"
TEXT = "#E8F4FF"
MUTED_COLOR = "#7890A8"

WIN_COLOR = "#FFD21F"
LOSE_COLOR = "#FF4264"
DRAW_COLOR = "#B85CFF"


# =========================================================
# ROOT
# =========================================================

root = tk.Tk()

root.title("Rock Paper Scissors")
root.configure(bg=BG_COLOR)

root.resizable(False, False)


# =========================================================
# CENTER WINDOW
# =========================================================

def center_window(window, width, height):

    window.update_idletasks()

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = int((screen_width - width) / 2)
    y = int((screen_height - height) / 2)

    window.geometry(
        f"{width}x{height}+{x}+{y}"
    )


# =========================================================
# SOUND
# =========================================================

# =========================================================
# SOUND
# =========================================================

def play_sound(filename):

    sound_path = os.path.join(
        SOUND_DIR,
        filename
    )

    if os.path.exists(sound_path):

        try:
            winsound.PlaySound(
                sound_path,
                winsound.SND_FILENAME |
                winsound.SND_ASYNC
            )

        except Exception:
            pass
# =========================================================
# BACKGROUND
# =========================================================

background = tk.Canvas(
    root,
    width=900,
    height=720,
    bg=BG_COLOR,
    highlightthickness=0
)

background.place(
    x=0,
    y=0
)


# =========================================================
# BACKGROUND LIGHTS
# =========================================================

background.create_oval(
    -180,
    20,
    300,
    520,
    fill="#061B2D",
    outline=""
)

background.create_oval(
    620,
    100,
    1100,
    600,
    fill="#160A2C",
    outline=""
)

background.create_oval(
    250,
    500,
    700,
    900,
    fill="#06152A",
    outline=""
)


# =========================================================
# TOP LINE
# =========================================================

background.create_line(
    80,
    8,
    820,
    8,
    fill=NEON_BLUE,
    width=2
)


# =========================================================
# CIRCLE 3D BUTTON
# =========================================================

class CircleButton:

    def __init__(
        self,
        parent,
        x,
        y,
        label,
        icon,
        command,
        accent
    ):

        self.parent = parent
        self.x = x
        self.y = y

        self.command = command
        self.accent = accent

        self.normal_offset = 0
        self.pressed = False

        self.current_label = label
        self.current_icon = icon

        self.canvas = tk.Canvas(
            parent,
            width=220,
            height=230,
            bg=BG_COLOR,
            highlightthickness=0
        )

        self.canvas.place(
            x=x,
            y=y
        )

        self.draw_button()

        self.canvas.bind(
            "<ButtonPress-1>",
            self.press
        )

        self.canvas.bind(
            "<ButtonRelease-1>",
            self.release
        )

        self.canvas.bind(
            "<Enter>",
            self.enter
        )

        self.canvas.bind(
            "<Leave>",
            self.leave
        )


    # =====================================================
    # DRAW BUTTON
    # =====================================================

    def draw_button(self):

        self.canvas.delete("all")

        offset = self.normal_offset

        # -----------------------------------------------
        # REALISTIC DARK SHADOW / DEPTH
        # -----------------------------------------------

        self.canvas.create_oval(
            18,
            18 + offset + 10,
            202,
            202 + offset + 10,
            fill="#010307",
            outline=""
        )

        # -----------------------------------------------
        # LOWER 3D DEPTH
        # -----------------------------------------------

        self.canvas.create_oval(
            13,
            13 + offset + 7,
            207,
            207 + offset + 7,
            fill="#020812",
            outline=self.accent,
            width=2
        )

        # -----------------------------------------------
        # MAIN CIRCLE
        # SAME INNER COLOR FOR ALL
        # -----------------------------------------------

        self.canvas.create_oval(
            15,
            15 + offset,
            205,
            205 + offset,
            fill=GLASS,
            outline=self.accent,
            width=2
        )
        # -----------------------------------------------
        # INNER CIRCLE
        # -----------------------------------------------

        self.canvas.create_oval(
            27,
            27 + offset,
            193,
            193 + offset,
            fill="#0B1A2B",
            outline=""
        )

        # -----------------------------------------------
        # SOFT INNER HIGHLIGHT
        # -----------------------------------------------

        self.canvas.create_oval(
            35,
            35 + offset,
            185,
            185 + offset,
            outline="#183149",
            width=1
        )

        # -----------------------------------------------
        # ICON
        # -----------------------------------------------

        self.canvas.create_text(
            110,
            88 + offset,
            text=self.current_icon,
            font=("Arial", 42),
            fill=WHITE
        )

        # -----------------------------------------------
        # LABEL
        # -----------------------------------------------

        self.canvas.create_text(
            110,
            145 + offset,
            text=self.current_label,
            font=("Arial", 14, "bold"),
            fill=WHITE
        )

        # -----------------------------------------------
        # SMALL NEON DOT
        # -----------------------------------------------

        self.canvas.create_oval(
            106,
            177 + offset,
            114,
            185 + offset,
            fill=self.accent,
            outline=""
        )


    # =====================================================
    # PRESS
    # =====================================================

    def press(self, event):

        if self.pressed:
            return

        self.pressed = True

        self.normal_offset = 7

        self.draw_button()


    # =====================================================
    # RELEASE
    # =====================================================

    def release(self, event):

        if not self.pressed:
            return

        self.pressed = False

        self.normal_offset = 0

        self.draw_button()

        self.command()


    # =====================================================
    # HOVER
    # =====================================================

    def enter(self, event):

        self.canvas.config(
            cursor="hand2"
        )


    def leave(self, event):

        self.canvas.config(
            cursor=""
        )


# =========================================================
# RESULT POPUP
# =========================================================

def show_result_popup(
    result,
    player_choice,
    computer_choice
):

    popup = tk.Toplevel(root)

    popup.title("Game Result")

    popup.resizable(
        False,
        False
    )

    popup.configure(
        bg=BG_COLOR
    )

    center_window(
        popup,
        460,
        410
    )

    popup.transient(root)

    popup.grab_set()


    # =====================================================
    # RESULT TYPE
    # =====================================================

    if result == "win":

        title = "YOU WIN!"
        title_color = WIN_COLOR
        sound = "Win.mp3"

    elif result == "lose":

        title = "YOU LOSE!"
        title_color = LOSE_COLOR
        sound = "Lose.mp3"

    else:

        title = "DRAW!"
        title_color = DRAW_COLOR
        sound = "Draw.mp3"


    # IMPORTANT:
    # Only result sound plays here.
    # Click.mp3 is NOT played here.

    play_sound(sound)


    # =====================================================
    # POPUP BACKGROUND
    # =====================================================

    canvas = tk.Canvas(
        popup,
        width=460,
        height=410,
        bg=BG_COLOR,
        highlightthickness=0
    )

    canvas.pack(
        fill="both",
        expand=True
    )


    canvas.create_oval(
        -120,
        -120,
        240,
        230,
        fill="#082A3B",
        outline=""
    )

    canvas.create_oval(
        260,
        -100,
        570,
        230,
        fill="#24103D",
        outline=""
    )


    # =====================================================
    # MAIN PANEL
    # =====================================================

    panel = tk.Frame(
        popup,
        bg=GLASS,
        highlightbackground=title_color,
        highlightcolor=title_color,
        highlightthickness=1
    )

    panel.place(
        x=20,
        y=20,
        width=420,
        height=370
    )


    # =====================================================
    # GAME RESULT
    # =====================================================

    tk.Label(
        panel,
        text="GAME RESULT",
        font=("Arial", 10, "bold"),
        bg=GLASS,
        fg=MUTED_COLOR
    ).pack(
        pady=(20, 3)
    )


    tk.Label(
        panel,
        text=title,
        font=("Arial", 28, "bold"),
        bg=GLASS,
        fg=title_color
    ).pack(
        pady=(2, 20)
    )


    # =====================================================
    # PLAYER
    # =====================================================

    player_card = tk.Frame(
        panel,
        bg=GLASS_2,
        highlightbackground=NEON_BLUE,
        highlightcolor=NEON_BLUE,
        highlightthickness=1
    )

    player_card.pack(
        fill="x",
        padx=30,
        pady=5
    )


    tk.Label(
        player_card,
        text=f"YOU     →     {player_choice}",
        font=("Arial", 12, "bold"),
        bg=GLASS_2,
        fg=WHITE
    ).pack(
        pady=11
    )
    # =====================================================
    # COMPUTER
    # =====================================================

    computer_card = tk.Frame(
        panel,
        bg=GLASS_2,
        highlightbackground=NEON_PURPLE,
        highlightcolor=NEON_PURPLE,
        highlightthickness=1
    )

    computer_card.pack(
        fill="x",
        padx=30,
        pady=5
    )


    tk.Label(
        computer_card,
        text=f"COMPUTER     →     {computer_choice}",
        font=("Arial", 12, "bold"),
        bg=GLASS_2,
        fg=WHITE
    ).pack(
        pady=11
    )


    # =====================================================
    # CONTINUE
    # =====================================================

    continue_button = tk.Button(
        panel,
        text="CONTINUE",
        font=("Arial", 10, "bold"),
        width=18,
        height=2,
        bg=NEON_BLUE,
        fg="#021018",
        activebackground=WHITE,
        activeforeground="#021018",
        relief="flat",
        bd=0,
        cursor="hand2",
        command=popup.destroy
    )

    continue_button.pack(
        pady=18
    )


# =========================================================
# UPDATE SCORE
# =========================================================

def update_score():

    score_label.config(
        text=(
            f"YOU: {player_score}"
            f"       COMPUTER: {computer_score}"
            f"       DRAW: {draw_score}"
        )
    )


# =========================================================
# GAME LOGIC
# =========================================================

def play_game(player_choice):

    global player_score
    global computer_score
    global draw_score


    computer_choice = random.choice(
        CHOICES
    )


    # =====================================================
    # DRAW
    # =====================================================

    if player_choice == computer_choice:

        draw_score += 1

        result = "draw"


    # =====================================================
    # WIN
    # =====================================================

    elif (
        (
            player_choice == "Rock"
            and computer_choice == "Scissors"
        )
        or
        (
            player_choice == "Paper"
            and computer_choice == "Rock"
        )
        or
        (
            player_choice == "Scissors"
            and computer_choice == "Paper"
        )
    ):

        player_score += 1

        result = "win"


    # =====================================================
    # LOSE
    # =====================================================

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
# RESET GAME
# =========================================================

def reset_game():

    global player_score
    global computer_score
    global draw_score


    play_sound(
        "Click.mp3"
    )


    player_score = 0
    computer_score = 0
    draw_score = 0


    update_score()


# =========================================================
# EXIT GAME
# =========================================================

def exit_game():

    play_sound(
        "Click.mp3"
    )


    answer = messagebox.askyesno(
        "Exit Game",
        "Are you sure you want to exit?",
        parent=root
    )


    if answer:

        root.destroy()


# =========================================================
# TITLE
# =========================================================

title_frame = tk.Frame(
    root,
    bg=BG_COLOR
)

title_frame.pack(
    pady=(25, 2)
)


tk.Label(
    title_frame,
    text="ROCK",
    font=("Arial", 31, "bold"),
    bg=BG_COLOR,
    fg=NEON_BLUE
).pack(
    side="left"
)


tk.Label(
    title_frame,
    text="  PAPER  ",
    font=("Arial", 31, "bold"),
    bg=BG_COLOR,
    fg=NEON_PURPLE
).pack(
    side="left"
)


tk.Label(
    title_frame,
    text="SCISSORS",
    font=("Arial", 31, "bold"),
    bg=BG_COLOR,
    fg=NEON_GOLD
).pack(
    side="left"
)


# =========================================================
# SUBTITLE
# =========================================================

tk.Label(
    root,
    text="CHOOSE YOUR MOVE",
    font=("Arial", 11, "bold"),
    bg=BG_COLOR,
    fg=NEON_CYAN
).pack(
    pady=2
)


# =========================================================
# SCORE PANEL
# =========================================================

score_shadow = tk.Frame(
    root,
    bg="#02050A"
)

score_shadow.pack(
    pady=14
)


score_frame = tk.Frame(
    score_shadow,
    bg=GLASS,
    highlightbackground=NEON_BLUE,
    highlightcolor=NEON_BLUE,
    highlightthickness=1
)

score_frame.pack(
    padx=2,
    pady=2
)


score_label = tk.Label(
    score_frame,
    text="YOU: 0       COMPUTER: 0       DRAW: 0",
    font=("Arial", 14, "bold"),
    bg=GLASS,
    fg=WHITE,
    padx=30,
    pady=13
)

score_label.pack()


# =========================================================
# CIRCLE BUTTON AREA
# =========================================================

game_area = tk.Frame(
    root,
    width=720,
    height=235,
    bg=BG_COLOR
)

game_area.pack(
    pady=8
)

game_area.pack_propagate(
    False
)


# =========================================================
# ROCK
# =========================================================

rock_button = CircleButton(
    game_area,
    0,
    0,
    "ROCK",
    "✊",
    lambda: play_game("Rock"),
    NEON_BLUE
)


# =========================================================
# PAPER
# =========================================================

paper_button = CircleButton(
    game_area,
    250,
    0,
    "PAPER",
    "✋",
    lambda: play_game("Paper"),
    NEON_PURPLE
)
# =========================================================
# SCISSORS
# =========================================================

scissors_button = CircleButton(
    game_area,
    500,
    0,
    "SCISSORS",
    "✌",
    lambda: play_game("Scissors"),
    NEON_GOLD
)


# =========================================================
# RESET + EXIT
# =========================================================

control_frame = tk.Frame(
    root,
    bg=BG_COLOR
)

control_frame.pack(
    pady=14
)


# =========================================================
# RESET BUTTON
# =========================================================

reset_button = tk.Button(
    control_frame,
    text="RESET GAME",
    font=("Arial", 10, "bold"),
    width=18,
    height=2,
    bg=GLASS,
    fg=NEON_BLUE,
    activebackground=NEON_BLUE,
    activeforeground="#021018",
    relief="flat",
    bd=0,
    highlightbackground=NEON_BLUE,
    highlightcolor=NEON_BLUE,
    highlightthickness=1,
    cursor="hand2",
    command=reset_game
)

reset_button.grid(
    row=0,
    column=0,
    padx=10
)


# =========================================================
# EXIT BUTTON
# =========================================================

exit_button = tk.Button(
    control_frame,
    text="EXIT",
    font=("Arial", 10, "bold"),
    width=18,
    height=2,
    bg=GLASS,
    fg=LOSE_COLOR,
    activebackground=LOSE_COLOR,
    activeforeground=WHITE,
    relief="flat",
    bd=0,
    highlightbackground=LOSE_COLOR,
    highlightcolor=LOSE_COLOR,
    highlightthickness=1,
    cursor="hand2",
    command=exit_game
)

exit_button.grid(
    row=0,
    column=1,
    padx=10
)


# =========================================================
# BUTTON HOVER
# =========================================================

def button_hover(
    button,
    normal_bg,
    hover_bg,
    normal_fg,
    hover_fg
):

    def enter(event):

        button.config(
            bg=hover_bg,
            fg=hover_fg
        )


    def leave(event):

        button.config(
            bg=normal_bg,
            fg=normal_fg
        )


    button.bind(
        "<Enter>",
        enter
    )

    button.bind(
        "<Leave>",
        leave
    )


button_hover(
    reset_button,
    GLASS,
    "#073B55",
    NEON_BLUE,
    WHITE
)


button_hover(
    exit_button,
    GLASS,
    "#4A101D",
    LOSE_COLOR,
    WHITE
)


# =========================================================
# BOTTOM DECORATIVE LINE
# =========================================================

bottom_canvas = tk.Canvas(
    root,
    width=600,
    height=25,
    bg=BG_COLOR,
    highlightthickness=0
)

bottom_canvas.pack(
    pady=(3, 0)
)


bottom_canvas.create_line(
    80,
    12,
    520,
    12,
    fill="#0A3048",
    width=1
)


bottom_canvas.create_oval(
    295,
    9,
    305,
    19,
    fill=NEON_BLUE,
    outline=""
)


# =========================================================
# START APPLICATION
# =========================================================

center_window(
    root,
    900,
    720
)

root.mainloop()