from tkinter import *
import random
import pandas as pd


BACKGROUND_COLOR = "#B1DDC6"
FRENCH_FONT = ('Ariel', 35, 'italic')
FRENCH_WORD_FONT = ('Ariel', 50, 'bold')
new_card = {}
data_dic = {}

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/_french_words.csv")
    print(original_data)
    data_dic = original_data.to_dict(orient="records")
else:
    data_dic = data.to_dict(orient="records")


def random_word():
    global new_card
    new_card = random.choice(data_dic)
    # print(new_card['French'])
    canvas.itemconfig(card_title, text ='French',fill='Black', font = FRENCH_FONT)
    canvas.itemconfig(card_word, text = new_card['French'], fill='Black', font = FRENCH_WORD_FONT)
    canvas.itemconfig(front_image, image=card_front)

def flip_card():
    canvas.itemconfig(card_title, text='English', fill='White', font=FRENCH_FONT)
    canvas.itemconfig(card_word, text=new_card['English'], fill='White', font=FRENCH_WORD_FONT)
    canvas.itemconfig(front_image, image=card_back)
    window.after(3000, flip_card)


def is_known():
    data_dic.remove(new_card)
    print(len(data_dic))
    data = pd.DataFrame(data_dic)
    data.to_csv("data/words_to_learn.csv", index=False)
    flip_card()


# ----------------------------  Create the User Interface (UI) with Tkinter ------------------------------- #
window = Tk()
window.title('Flashy')
window.config(padx=50, pady=100, background=BACKGROUND_COLOR)

## Front card
canvas = Canvas(width=800, height=526)
canvas.pack()
card_front = PhotoImage(file="images\card_front.png")
card_back = PhotoImage(file="images\card_back.png")
front_image = canvas.create_image(410,275, image =card_front)
card_title = canvas.create_text(410,150, text='', font=FRENCH_FONT)
card_word = canvas.create_text(410,263, text='', font=FRENCH_WORD_FONT)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

## Right Button
right_button_image = PhotoImage(file='images\_right.png')
right_button = Button(window,image=right_button_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

wrong_button_image = PhotoImage(file='images\wrong.png')
wrong_button = Button(padx=50,image=wrong_button_image, highlightthickness=0, command=random_word)
wrong_button.grid(row=1, column=0)


random_word()
window.after(3000, flip_card)
window.mainloop()

