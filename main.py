from turtle import Turtle, Screen
import pandas
data = pandas.read_csv("50_states.csv")
s=Screen()
s.title("us states")
t= Turtle()
img = "blank_states_img.gif"
s.addshape(img)
t.shape(img)
states=data.state.to_list()
guess = []
while len(guess)<50:
    name=s.textinput(title=f"{len(guess)}/50, guess the state",prompt="what is your next state?").title()
    if name == "Exit":
        missinglist=[i for i in states if i not in guess ]
        new_data=pandas.Series(missinglist)
        new_data.to_csv("Unguessed states.csv")
        exit()
    if name in states:
        guess.append(name)
        newt= Turtle()
        newt.hideturtle()
        newt.penup()
        cordlist=data[data.state == name].to_dict()
        ind = states.index(name)
        xcor = cordlist["x"][ind]
        ycor = cordlist["y"][ind]
        newt.goto(xcor, ycor)
        newt.write(name)
    # elif name == "Exit":
    #     for i in guess:
    #         if i in states:
    #             states.pop(states.index(i))
    #     new_data=pandas.Series(states)
    #     new_data.to_csv("Unguessed states.csv")
    #     exit()    
s.mainloop()