import turtle
import pandas as pd


def create_state_df():
    df = pd.read_csv('50_states.csv')
    return df


def insert_state(answer, x, y):
    state.goto(x, y)
    state.write(answer, align='center', font=("courier", 12, "normal"))



guessed_states = []
image = 'blank_states_img.gif'

screen = turtle.Screen()
screen.title('U.S States Game')
screen.addshape(image)

turtle.shape(image)


state_df = create_state_df()
state_list = state_df.state.to_list()
state = turtle.Turtle()
state.hideturtle()
state.penup()

is_game_on = True
while len(guessed_states) <= 50:

    answer_state = screen.textinput(title=f'{score}/50 Guess the State', prompt='What is the name of the state: \n')

    if answer_state in state_list:
        answer_df = state_df[state_df.state == answer_state]
        insert_state(answer_state, int(answer_df.x), int(answer_df.y))
        guessed_states.append(answer_state)
turtle.mainloop()
