from turtle import Screen
import turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import random

screen = Screen()
screen.bgcolor("black")
screen.screensize(600,600)
screen.title("Snake game!")
screen.listen()
screen.tracer(0)
high_score = 0
scoreboard = Scoreboard()
wall = Scoreboard()
wall.wall()
snake = Snake()
food = Food()
game_is_on = True
current_score = 0
while game_is_on:
    snake.move()
    if snake.body[0].distance(food) == 0:
        food.relocate(snake.block)
        current_score += 1
        scoreboard.score(current_score)
        if current_score > high_score:
            high_score += 1
        if current_score == 29*29:
            print("You win!!!!!")
        else:
            snake.eat()

    if (snake.block[0][0] < -280) or (snake.block[0][0] > 280) or (snake.block[0][1] < -280) or (snake.block[0][1] > 280):
        game_is_on = False
        snake.body[0].hideturtle()
        scoreboard.gameover()

    for i in range(1,len(snake.block)):
        if snake.block[0] == snake.block[i]:
            game_is_on = False
            scoreboard.gameover()




screen.exitonclick()









