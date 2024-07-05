from turtle import *
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time
s=Screen()
s.tracer(0)
segments=[]
s.setup(width=600,height=600)
s.bgcolor("black")
s.title("my snake game")
snake=Snake()
food=Food()
score_board=ScoreBoard()
s.listen()
s.onkey(snake.up,"Up",)
s.onkey(snake.down,"Down")
s.onkey(snake.left,"Left")
s.onkey(snake.right,"Right")
game_is_on=True
while game_is_on:
    time.sleep(0.1)
    s.update()
    snake.move()
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        score_board.increase_score()
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        game_is_on=False
        score_board.game_over()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            game_is_on=False
            score_board.game_over()


















s.exitonclick()