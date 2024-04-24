from quiz_brain import QuizBrain
from user import User


if __name__ == "__main__":
    user = User()
    quiz = QuizBrain()
    while quiz.still_has_question():
        choice = quiz.ask_question()
        if quiz.check_answer(choice):
            user.correct_answer += 1
        user.question_count += 1
        user.report()
        quiz.pop_question()

    print("You've completed the quiz")
    print(f"You finish the score with a total of {user.correct_answer}/{user.question_count}")