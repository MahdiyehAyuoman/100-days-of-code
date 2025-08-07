

class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0


    def still_has_question(self):

        total_list_len = self.question_number
        question_list_len = len(self.question_list)

        if total_list_len < question_list_len:
            return True
        else:
            return False


    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number+=1

        question_answer = question.answer
        user_answer = input(f"Q{self.question_number}: {question.text} (True/False)")

        self.check_answer(user_answer, question_answer)


    def check_answer(self, user_answer, question_answer):
        if user_answer.lower() == question_answer.lower():
            self.score += 1
            print("Your answer is corect")
            print(f"Currect answer is: {question_answer}")
            # print(f"Your current score is {self.score} / {self.question_number}")
        else:
            
            print("Your answer isn't corect")
            print(f"Currect answer is: {question_answer}")
        print(f"Your current score is: {self.score} / {self.question_number}")
        print("\n")




        


