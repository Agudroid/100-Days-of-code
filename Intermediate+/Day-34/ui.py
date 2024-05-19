from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Trivia App")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="white", font=("Arial", 12, "bold"))
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="White")
        self.question_text = self.canvas.create_text(
            150,
            120,
            width=250,
            text="Question Test",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_photo = PhotoImage(file='images/true.png')
        self.true_button = Button(image=true_photo, highlightthickness=0, command=self.check_true)
        self.true_button.grid(row=2, column=0)

        false_photo = PhotoImage(file='images/false.png')
        self.false_button = Button(image=false_photo, highlightthickness=0, command=self.check_false)
        self.false_button.grid(row=2, column=1)

        self.get_question()

        self.window.mainloop()

    def get_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            question = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question)
        else:
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
            self.canvas.itemconfig(self.question_text, text="You finish the Test !!")
    def check_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def check_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def give_feedback(self, is_right):
        color = "green" if is_right else "red"
        self.canvas.config(bg=color)
        self.window.after(500, self.get_question)


