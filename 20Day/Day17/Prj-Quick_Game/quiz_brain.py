class QuizBran:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.scores = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(
            f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_question(user_answer, current_question)

    def check_question(self, user_answer, question):
        if user_answer.lower() == question.answer.lower():
            self.scores += 1
            print("You got right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {question.answer}")
        print(f"your current score is: {self.scores} / {self.question_number}")
