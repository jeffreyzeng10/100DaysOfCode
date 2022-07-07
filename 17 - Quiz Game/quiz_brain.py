class QuizBrain():
    def __init__(self, q_list):
        self.question_number = 0
        self.questions_list = q_list
        self.score = 0
    
    def check_answer(self, user_answer, answer):
        return user_answer == answer
        
    def show_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number+=1
        response = input(f'Q{self.question_number}: {current_question.text}. (True/False)?: ')
        if self.check_answer(response, current_question.answer):
            print("You got it right!")
            self.score+=1
        else:
            print("You got it wrong!")
        print(f'The correct answer was: {current_question.answer}')
    
    def still_has_questions(self):        
        return self.question_number < len(self.questions_list)

    def show_score(self):
        print(f'Your current score is: {self.score}/{self.question_number}')


