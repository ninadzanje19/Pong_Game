from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

pong_screen = Screen()
pong_screen.title("Pong Game")
pong_screen.bgcolor("black")
pong_screen.setup(width=800, height=600)
pong_screen.tracer(0)
game_ball = Ball()
game_score = Scoreboard()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

pong_screen.listen()
pong_screen.onkey(r_paddle.go_up, "Up")
pong_screen.onkey(r_paddle.go_down, "Down")

pong_screen.onkey(l_paddle.go_up, "w")
pong_screen.onkey(l_paddle.go_down, "s")

game_on = True
while game_on:
    pong_screen.update()
    game_ball.move()
    time.sleep(0.1)


    if game_ball.ycor() > 280 or game_ball.ycor() < - 280:
        game_ball.bounce_top()

    if game_ball.distance(r_paddle) < 50 and game_ball.xcor() > 320 or game_ball.distance(l_paddle) < 50 and game_ball.xcor() < -320:
        game_ball.bounce_side()

    if game_ball.xcor() > 380:
        game_ball.reset_pos()
        game_ball.bounce_side()
        game_score.l_point()

    if game_ball.xcor() < -380:
        game_ball.reset_pos()
        game_ball.bounce_side()
        game_score.r_point()

pong_screen.exitonclick()
