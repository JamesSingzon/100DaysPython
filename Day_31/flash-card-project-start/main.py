from tkinter import *
import pandas
from random import choice



# ---------------------------- WORD DATABASE ------------------------------- #
word_db = pandas.read_csv("data/french_words.csv")
word_dict = word_db.to_dict(orient="records")
current_card = {}

def new_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(word_dict)
    print(current_card)
    print(word_dict.index(current_card))

    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    canvas.itemconfig(flash_img, image=card_front)
    flip_timer = window.after(3000, flash_word)


def flash_word():
    global current_card
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")
    canvas.itemconfig(flash_img, image=card_back)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 




# ---------------------------- UI SETUP ------------------------------- #

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")


# GUI
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, flash_word)

# FRONT FLASH CARD CANVAS
canvas = Canvas(highlightthickness=0, width=800, height=526, bg=BACKGROUND_COLOR)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")

flash_img = canvas.create_image(400, 263, image=card_front)
language_text = canvas.create_text(400, 150, text="", fill="black", font=LANGUAGE_FONT)
word_text = canvas.create_text(400, 263, text="", fill="black", font=WORD_FONT)
canvas.grid(column=0, row=0, columnspan=2)

# BACK FLASH CARD CANVAS
# canvas = Canvas(highlightthickness=0, width=800, height=526, bg=BACKGROUND_COLOR)
# card_back = PhotoImage(file="images/card_back.png")
# canvas.create_image(400, 263, image=card_front)
# language_text = canvas.create_text(400, 150, text="French", fill="black", font=LANGUAGE_FONT)
# word_text = canvas.create_text(400, 263, text="trouve", fill="black", font=WORD_FONT)
# canvas.grid(column=0, row=0, columnspan=2)

# CORRECT BUTTON
correct = PhotoImage(file="images/right.png")
correct_button = Button(image=correct, highlightthickness=0, command=new_word)
correct_button.grid(column=1, row=1)

# INCORRECT BUTTON
incorrect = PhotoImage(file="images/wrong.png")
incorrect_button = Button(image=incorrect, highlightthickness=0, command=new_word)
incorrect_button.grid(column=0, row=1)

new_word()

window.mainloop()
