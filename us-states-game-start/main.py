import turtle
import pandas as pd

screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

mr_draw = turtle.Turtle()
mr_draw.penup()
mr_draw.hideturtle()

states_df = pd.read_csv('50_states.csv')
guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name").title()
    if answer_state == 'Exit':
        break
    for state in states_df.state:
        if state == answer_state and answer_state not in guessed_states:
            answer_row = states_df[states_df['state'].str.contains(answer_state)]
            mr_draw.goto(answer_row.iat[0, 1], answer_row.iat[0, 2])
            mr_draw.write(answer_row.iat[0, 0])
            guessed_states.append(answer_state)


all_states = states_df.state.to_list()
states_to_learn = [state for state in all_states if state not in guessed_states]
learning_csv = pd.DataFrame(states_to_learn).to_csv()

with open('learn.csv', mode='w', newline='') as file:
    file.write(learning_csv)
