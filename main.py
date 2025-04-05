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
while len(Gussed_state) < 5:
    answer_state = screen.textinput(title="Gusse the state", prompt="Which one is next state")
    if answer_state in all_states:
        Gussed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)


screen.exitonclick()
