import data
from question_model import Question
from quiz_brain import QuizBran


def create_list_question(data):
    question_bank = []
    for question in data:
        question_bank.append(Question(question['text'], question['answer']))
    return question_bank


question_bank = create_list_question(data.question_data)
quiz = QuizBran(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz")
print(f"Youre final score was: {quiz.scores} / {len(question_bank)}")
