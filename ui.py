from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
FONT = ("Arial", 15, "italic")


class Ui:

    def __init__(self, quiz_brain: QuizBrain):
        self.isover = False
        self.quiz = quiz_brain
        self.tk = Tk()
        self.tk.config(padx=20, pady=20, bg=THEME_COLOR)
        self.tk.title("Quizzler")
        self.score = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        t_photo = PhotoImage(file=".\images\\true.png")
        w_photo = PhotoImage(file=".\images\\false.png")
        self.right = Button(image=t_photo, highlightthickness=0, borderwidth=0, command=self.right)
        self.wrong = Button(image=w_photo, highlightthickness=0, borderwidth=0, command=self.wrong)
        self.canvas = Canvas(height=250, width=300)
        self.question = self.canvas.create_text(150, 125, font=FONT, width=280)
        self.score.grid(row=0, column=1)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.right.grid(row=2, column=0)
        self.wrong.grid(row=2, column=1)
        self.get_next()
        self.tk.mainloop()

    def get_next(self):
        n_quiz = self.quiz.next_question()
        self.canvas.itemconfig(self.question, text=n_quiz)

    def right(self):
        if not self.isover:
            ans = "True"
            vali_ans = self.quiz.check_answer(ans)
            if vali_ans:
                self.canvas.config(bg="green")
                self.tk.after(1000, self.background_color)

            else:
                self.canvas.config(bg="red")
                self.tk.after(1000, self.background_color)

        else:
            self.tk.destroy()

    def wrong(self):
        if not self.isover:
            ans = "False"
            vali_ans = self.quiz.check_answer(ans)
            if vali_ans:
                self.canvas.config(bg="green")
                self.tk.after(1000, self.background_color)

            else:
                self.canvas.config(bg="red")
                self.tk.after(1000, self.background_color)

        else:
            self.tk.destroy()

    def score_update(self):
        self.score.config(text=f"Score: {self.quiz.score}")

    def background_color(self):
        self.canvas.config(bg="white")
        self.score_update()
        if self.quiz.still_has_questions():
            self.get_next()
        else:
            self.canvas.itemconfig(self.question, text=f"You've completed the quiz\n"
                                                       f"Your final score is {self.quiz.score}/"
                                                       f"{self.quiz.question_number}"
                                                       f"\nPress any button to close")
            self.isover = True
