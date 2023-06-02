
class QuizBrain:
    
    def __init__(self,q_list) -> None:
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    
    def next_question(self):
        self.answer = input(f"Q.{self.question_number + 1}: {self.question_list[self.question_number].text} (True/False)?: ")
        self.check_answer()
        self.question_number += 1

    def check_answer(self):
        if self.answer.lower() == self.question_list[self.question_number].answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {self.question_list[self.question_number].answer}.")
        print(f"Score: {self.score}/{self.question_number + 1}")
        print()

