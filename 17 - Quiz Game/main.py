from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

# create list of question objects
question_list = []
for i in question_data:
    question = Question(i['text'], i['answer'])
    question_list.append(question)

quiz = QuizBrain(question_list)
while quiz.still_has_questions():
    quiz.show_question()
    quiz.show_score()

print("You've completed the quiz!")
print(f'Your final score was {quiz.score}/{len(question_list)}')
