import turtle
import pandas
import time


#Already gathered coor from given directory files.
# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)

# turtle.mainloop()

start_time = time.time()
state_list = []
data = pandas.read_csv("Day_25/us-states-game-start/50_states.csv")


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "Day_25/us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

def pin_state(state_coor, answer_state):
    '''Generates the state name on screen and pins to state coordinates.'''
    tim = turtle.Turtle()
    tim.hideturtle()
    tim.pu()
    tim.goto(state_coor)
    tim.write(f"{answer_state}", align="center",font=("Courier",15,"normal"))

def save_score(state_list, data):
    '''Saves the player's score to a csv.'''
    states_missed_list = [state for state in data["state"].to_list() if state not in state_list]
    score_dict = {
        "player": screen.textinput(title=f"You guessed {len(state_list)}/{len(data)} states correct", prompt="Type your name to save your score.").title(),
        "score": f"{len(state_list)}/{len(data)}",
        "states_missed": states_missed_list
    }
    with open("Day_25/us-states-game-start/high_scores.txt", mode="a") as scores:
        scores.write(f"{score_dict}\n")



game_on = True
while len(state_list) < 50 and game_on:
    answer_state = screen.textinput(title=f"{len(state_list)}/{len(data)} States Correct", prompt="What's another state's name?").title()
    if answer_state in data["state"].to_list()and answer_state not in state_list:
        state_list.append(answer_state)
        state_coor = (int(data[data.state == answer_state]["x"]), int(data[data.state == answer_state]["y"]))
        pin_state(state_coor, answer_state)

    if time.time() - start_time >= 600 or answer_state == "Exit":
        game_on = False

save_score(state_list, data)

screen.exitonclick()