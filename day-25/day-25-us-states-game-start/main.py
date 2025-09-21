import turtle
import pandas as pd

FONT =("Arial", 10, "bold")

screen = turtle.Screen()
write_state = turtle.Turtle()
write_state.hideturtle()
write_state.penup()
screen.title("U.S States Game")
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

user_correct_guess = 0
state_number = 51

states_csv = pd.read_csv('50_states.csv')
state = states_csv['state']

user_correct_guess_list = []
state_to_learn = []
for count in range(state_number):
    answer_state = screen.textinput(title=f'{user_correct_guess}/50 States Correct', prompt="What's another state's name?").title()
    if answer_state == 'Exit':
        for s in state:
            if s not in user_correct_guess_list:
                state_to_learn.append(s)
        break
    for s in state:
        if s == answer_state and s not in user_correct_guess_list:
            user_correct_guess+=1
            print(user_correct_guess) 

            ## Check the user's guess with the name State to choose the position of x and y
            state_row = states_csv[states_csv['state'] == answer_state]
            x_coordinate = int(state_row['x'].iloc[0])
            y_coordinate = int(state_row['y'].iloc[0])
            user_correct_guess_list.append(s)
            write_state.goto(x_coordinate, y_coordinate)
            write_state.write(f'{s}', align='center', font=FONT)
            print(user_correct_guess_list)

# # dictionary of state to learn, save as csv file
state_to_learn_dic = {'state': state_to_learn}
state_to_learn = pd.DataFrame(state_to_learn_dic)
state_to_learn.to_csv('state_to_learn.csv', index=False,header=True)
# print(state_to_learn)