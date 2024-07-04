import html
# import ui


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None
        # self.ui = ui.Ui()

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        self.current_question.text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {self.current_question.text} (True/False): "
        # self.ui.canvas.itemconfig(self.ui.question, text=f"{self.question_number}: {self.current_question}")
        # self.check_answer(user_answer)

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
            print(f"Your current score is: {self.score}/{self.question_number}")
            print("\n")
            return True
        else:
            print(f"Your current score is: {self.score}/{self.question_number}")
            print("\n")
            print("That's wrong.")
            return False


