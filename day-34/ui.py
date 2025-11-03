from tkinter import *
from quiz_brain import QuizBrain
from data import question_data

THEME_COLOR = "#375362"
FONT = ('Arial', 15, 'italic')

class QuizInterface:
    def __init__(self, quize_brain: QuizBrain):

        self.quize = quize_brain
        self.window = Tk()
        self.title = self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_text = Label(text=f'Score: {0}',bg=THEME_COLOR, fg='white')
        self.score_text.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125, width=280,text="some text", font=FONT, fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image,highlightthickness=0, command=self.true_answer)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image,highlightthickness=0, command=self.false_answer)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(background='white')
        if self.quize.still_has_questions():
            self.score_text.config(text=f'Score: {self.quize.score}')
            q_text = self.quize.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz!")
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')


    def true_answer(self):
        true_answer = self.quize.check_answer('True')
        self.get_feedback(true_answer)

    def false_answer(self):
        false_answer = self.quize.check_answer("False")
        self.get_feedback(false_answer)

    def get_feedback(self, false_answer):
        
        if false_answer:
            self.canvas.config(background='green')
        else:
            self.canvas.config(background='red')
        self.window.after(1000, self.get_next_question)
