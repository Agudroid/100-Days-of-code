from data import question_data
from question_model import QuestionModel
from user import User
from random import shuffle


class QuizBrain:

    def __init__(self):
        self.question_list = []
        self.total_questions = len(question_data)
        self.questions_asked = 0
        shuffle(question_data['results'])
        for questions in question_data['results']:
            model = QuestionModel(questions['question'], questions['correct_answer'])
            self.question_list.append(model)

    def still_has_question(self):
        return len(self.question_list) > 0

    def ask_question(self):
        self.questions_asked += 1
        return input(f"Q.{self.questions_asked}: {self.question_list[0].question} (True/False):")

    def pop_question(self):
        self.question_list.pop(0)

    def check_answer(self, answer):
        return self.question_list[0].answer == answer
