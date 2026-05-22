from turtle import Screen
from names import Names
from paddle import Paddle
from ball import Ball
from score import Score
import time

window = Screen()
window.title("First Ping Pong")
window.bgcolor("black")
window.setup(800,600)
window.tracer(0)


r_player= window.textinput("First player","Enter your name please:").upper()
r_name = Names((330,240),r_player)
r_paddle = Paddle((350 , 0))

l_player = window.textinput("2nd player","Enter your name please:").upper()
l_name = Names((-330,240),l_player)
l_paddle = Paddle((-350 , 0))

ball = Ball()
score_r = Score((150 , 250))
score_l = Score((-150 , 250))

 
game_on = True
window.listen()


window.onkey(r_paddle.go_up , "Up")
window.onkey(r_paddle.go_down , "Down")

window.onkey(l_paddle.go_up , "w")
window.onkey(l_paddle.go_down , "s")

default_sleep = 0.1
while game_on:
    window.update()
    time.sleep(0.04)

    ball.move_ball()


    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.y_move *= -1

    if (ball.xcor() >= 330 and ball.distance(r_paddle) <= 50) or (ball.xcor() <= -330 and ball.distance(l_paddle) <= 50):
        ball.x_move *= -1
        default_sleep *= 0.9
        
      
    if ball.xcor() > 400:
        ball.goto(0,0)
        score_l.increase_score()
        ball.x_move *= -1
        default_sleep = 0.1
        
    if ball.xcor() < -400:
        ball.goto(0,0)
        score_r.increase_score()
        ball.x_move *= -1
        default_sleep = 1


    if score_r.new_score() == 11:
        score_r.game_over(r_player)
        break
    
    if score_l.new_score() == 11:
        score_l.game_over(l_player)
        break
    

window.exitonclick()
