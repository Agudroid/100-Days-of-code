import turtle
import pandas as pd


def create_state_df():
    df = pd.read_csv('50_states.csv')
    return df


def insert_state(answer, x, y):
    state.goto(x, y)
    state.write(answer, align='center', font=("courier", 12, "normal"))

def initialize_states(guessed_states, state_df):
    global score
    score += len(guessed_states)
    while len(guessed_states) > 0:
        state_name = guessed_states.pop(0)
        state = state_df[state_df.state == state_name]
        insert_state(state_name, int(state.x), int(state.y))


score = 0
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

guessed_states_df = pd.read_csv('saved_states.csv')
print(guessed_states_df)

if not guessed_states_df.empty:
    guessed_states = guessed_states_df['0'].to_list()
    print(guessed_states)
    initialize_states(guessed_states, state_df)
else:
    guessed_states = []

is_game_on = True
while len(guessed_states) <= 50 and is_game_on:

    answer_state = screen.textinput(title=f'{score}/50 Guess the State', prompt='What is the name of the state: \n')

    if answer_state in state_list:
        answer_df = state_df[state_df.state == answer_state]
        insert_state(answer_state, int(answer_df.x), int(answer_df.y))
        guessed_states.append(answer_state)
        score += 1
    elif answer_state == 'exit':
        pd.DataFrame(guessed_states).to_csv('saved_states.csv')
        is_game_on = False
turtle.mainloop()
