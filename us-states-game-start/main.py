import turtle
from turtle import Turtle, Screen
import pandas
ALIGNMENT = "center"
FONT = ("Courier", 10, "bold")
game_on = True
data = pandas.read_csv("50_states.csv")
cor = 0
screen =Screen()
usa = Turtle()
screen.title("USA Game")

screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

def create_text_state():
    nameofstate = answer_state
    locals()[nameofstate]=Turtle()
    locals()[nameofstate].penup()
    locals()[nameofstate].hideturtle()

    xcord = data[data.state == answer_state.title()]
    x = float(xcord.x)
    ycord = data[data.state == answer_state.title()]
    y = float(ycord.y)
    print(x)
    print(y)
    locals()[nameofstate].goto(x, y)
    locals()[nameofstate].write(nameofstate, align=ALIGNMENT, font=FONT )

correct = []







while len(correct) < 50 :
    hm = len(correct)
    answer_state = screen.textinput(title = f"{hm}/50", prompt="Whats the state name?").title()


    if answer_state.lower() == "exit":
        dragon = []
        print("part 1")
        for missing_words in data.state:
            print("part 2")
            if missing_words not in correct:
                print("part 3")
                dragon.append(missing_words)
        print("part 4")
        new_data = pandas.DataFrame(dragon)
        new_data.to_csv("states_to_learn.csv")

        break
    for word in data.state:
        if answer_state == word:
            print(answer_state)
            print(word)
            print("part1")
            if answer_state not in correct:
                    print("part3")
                    correct.append(answer_state)
                    print("well done")
                    print(correct)
                    create_text_state()
            else:
                print("this is already on the map")










