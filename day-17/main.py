from data import question_data
from question_model import Quastion
from quiz_brain import QuizBrain


question_bank = []  ## bank of the all questions & answers

## create bank of questions by Question Class
for item in question_data:
    # print(item['text'])
    question_text = item['text']
    question_answer = item['answer']
    

    each_item = Quastion(question_text, question_answer)
    # print(each_item.text)
    question_bank.append(each_item)

# print(question_bank)

## Creat a quiz game by QuizBrain Class
game = QuizBrain(question_bank)

# print(game.next_question())
# print(game.still_has_question())

countinue_game = True

# while loop quiz game
while countinue_game:
    if game.still_has_question():
        game.next_question()
    else:
        countinue_game = False
        print("You've completed the quiz")
        print(f"Your final score was: {game.score}/{len(question_bank)}")




