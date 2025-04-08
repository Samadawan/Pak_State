import turtle
import pandas

screen = turtle.Screen()
screen.title("5 States of PAK")
image = "PAK.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("5_states.csv")
all_states = data.state.to_list()
Gussed_state =[]
while len(Gussed_state) < len(all_states):
    answer_state = screen.textinput(title=f"{len(Gussed_state)}/{len(all_states)} States Correct", prompt="Which one is next state").title()
    if answer_state in all_states:
        Gussed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)



screen.exitonclick()
