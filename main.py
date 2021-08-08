from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import Score
import time




screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
screen.listen()
lpaddle = Paddle((-370, 0))
rpaddle = Paddle((370, 0))
game_ball = Ball()
score_writer = Turtle()
score_writer.hideturtle()
user1_score = Score((270, 270), "Player1")
user2_score = Score((-270, 270), "Player2")
screen.onkey(fun=rpaddle.up, key="Up", )
screen.onkey(fun=rpaddle.down, key="Down")
screen.onkey(fun=lpaddle.up, key="w", )
screen.onkey(fun=lpaddle.down, key="s")
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    game_ball.move()
    if game_ball.ycor() > 280 or game_ball.ycor() < -280:
        game_ball.bounce()
    if game_ball.xcor() > 380 or game_ball.xcor() < -380:
        is_game_on = False
        game_ball.game_over()
        if user1_score.score > user2_score.score:
            score_writer.penup()
            score_writer.goto(0,270)
            score_writer.color("green")
            score_writer.write(f"{user1_score.username} wins", align="center", font=('Courier', 15, 'normal'))
        elif user2_score.score > user1_score.score:
            score_writer.penup()
            score_writer.goto(0,270)
            score_writer.color("green")
            score_writer.write(f"{user2_score.username} wins", align="center", font=('Courier', 15, 'normal'))
        else:
            score_writer.penup()
            score_writer.goto(0, 270)
            score_writer.color("green")
            score_writer.write(f"DRAW", align="center", font=('Courier', 15, 'normal'))

    if game_ball.distance(lpaddle) < 40 and game_ball.xcor() < -340:
        game_ball.collision()
        user2_score.increase_score()
    elif game_ball.distance(rpaddle) < 40 and game_ball.xcor() > 340:
        game_ball.collision()
        user1_score.increase_score()


screen.exitonclick()