from turtle import Turtle , Screen

class Score(Turtle):
    def __init__(self , positions):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(positions)
        self.pendown()
        self.beg_score()

    def beg_score(self):
        self.write(f"{self.score}", align = "center", font = ("Arial",40,"normal"))


    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"{self.score}", align = "center", font = ("Arial",40,"normal"))


    def new_score(self):
        return self.score
        

    def game_over(self,name):
        self.penup()
        self.goto(0,0)
        self.pendown()
        self.color("red")
        self.write(f"{name} Is The Winner!!!",align = "center", font = ("Arial",40,"normal"))
