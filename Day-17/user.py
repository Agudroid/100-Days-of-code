class User:
    def __init__(self):
        self.question_count = 0
        self.correct_answer = 0

    def report(self):
        print(f"You have answered correctly {self.correct_answer}/{self.question_count}.")
