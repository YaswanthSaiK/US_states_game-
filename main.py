import turtle
import pandas
data = pandas.read_csv("50_states.csv")
hub = turtle.Turtle()
hub.penup()
hub.hideturtle()

screen = turtle.Screen()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
con = True
lis = []
n = 0
while con:
    guess = turtle.textinput(title=f"{n}/50 states are correct", prompt="guess the another state!").title()
    if guess == "Exit":
        # li = []
        # for j in data["state"]:
        #     if j not in lis:
        #         if j not in li:
        #             li.append(j)
        li = [j for j in data["state"] if j not in lis]
        dic = {"state": li}
        j = pandas.DataFrame(dic)
        j.to_csv("states_to_learn.csv")
        break
    for i in data["state"]:
        if i == guess:
            if guess not in lis:
                hub.goto(float(data[data["state"] == guess]["x"]), float(data[data["state"] == guess]["y"]) )
                hub.write(guess)
                lis.append(guess)
                n += 1
                if n == 50:
                    con = False

screen.exitonclick()


