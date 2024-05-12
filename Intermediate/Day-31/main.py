from tkinter import *
from data import FlashCard, FlashCardDeck
BACKGROUND_COLOR = "#B1DDC6"


cards = FlashCardDeck()
selected_card = cards.pick_card()
reps = 0
count_global = 0


def start():
    global reps
    reps += 1
    flip_card(180)



def flip_card(count):
    global selected_card
    if count <= 0:
        if reps % 2 == 0:
            selected_card = cards.pick_card()
            back_image = PhotoImage(file='images/card_front.png')
            canvas.itemconfig(canvas_image, image=back_image)
            canvas.itemconfig(language_text, text="French", fill="Black")
            print(selected_card.question)
            canvas.itemconfig(word, text=selected_card.question, fill="Black")
            start()
        else:
            back_image = PhotoImage(file='images/card_back.png')
            canvas.itemconfig(canvas_image, image=back_image)
            canvas.itemconfig(language_text, text="English", fill="White")
            print(selected_card.answer)
            canvas.itemconfig(word, text=selected_card.answer, fill="White")
            start()
    else:
        window.after(3, flip_card, count-1)


def word_learned():
    global reps
    reps = 0

    cards.remove_card(selected_card)


# UI Design
def print_card():
    global selected_card
    selected_card = cards.pick_card()


window = Tk()
window.title("Flash Cards App")
window.config(height=600, width=1000, padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file='images/card_front.png')
canvas_image = canvas.create_image(405, 260, image=front_image)
language_text = canvas.create_text(400, 150, text='French', font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text=selected_card.question, font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong_image = PhotoImage(file='images/wrong.png')
cross_button = Button(image=wrong_image, highlightthickness=0, command=print_card)
cross_button.grid(row=1, column=0)

right_image = PhotoImage(file='images/right.png')
right_button = Button(image=right_image, highlightthickness=0, command=word_learned)
right_button.grid(row=1, column=1)

start()

window.mainloop()