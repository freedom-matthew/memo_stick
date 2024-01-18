from tkinter import *
from pandas import *
from random import *

BACKGROUND_COLOR = "#B1DDC6"


# region BUTTONS
def next_card():
    current_card = choice(to_learn)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=current_card["French"])


# endregion
# region DATA setup
data = read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")
print(to_learn)
# endregion
# region UI setup
window = Tk()
window.title("MemoStick")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card_image = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=front_card_image)
card_title = canvas.create_text(400, 100, font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2, sticky="ew")

cross_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=cross_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
right_button = Button(image=check_image, highlightthickness=0, command=next_card)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()
# endregion
