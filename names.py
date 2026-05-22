from turtle import Turtle, Screen

class Names(Turtle):
    def __init__(self,postions,name):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("green")
        self.goto(postions)
        self.pendown()
        self.write(f"{name}", align = "center" , font = ("Arial",24,"normal"))