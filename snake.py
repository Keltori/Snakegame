from turtle import Turtle, Screen
import time
screen = Screen()
screen.listen()

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        self.length = 3
        self.body = []
        self.block = []

        for i in range(3):
            new_turtle = Turtle("square")
            new_turtle.penup()
            new_turtle.color("white")
            new_turtle.setpos(-20 * i, 0)
            self.body.append(new_turtle)
            self.block.append(new_turtle.pos())


    def up(self):
        if self.body[1].pos() != (self.body[0].xcor(), self.body[0].ycor() + 20) :
            self.body[0].setheading(UP)

    def down(self):
        if self.body[1].pos() != (self.body[0].xcor(), self.body[0].ycor() - 20):
            self.body[0].setheading(DOWN)

    def left(self):
        if self.body[1].pos() != (self.body[0].xcor() -20, self.body[0].ycor()):
            self.body[0].setheading(LEFT)

    def right(self):
        if self.body[1].pos() != (self.body[0].xcor()  + 20, self.body[0].ycor()):
            self.body[0].setheading(RIGHT)

    def move(self):
        screen.update()
        time.sleep(0.1)
        for i in range(len(self.body)-1, 0, -1):
            self.body[i].setpos(self.body[i-1].pos())

        screen.onkey(self.up, "w")
        screen.onkey(self.down, "s")
        screen.onkey(self.left, "a")
        screen.onkey(self.right, "d")
        if self.body[0].heading() == RIGHT:
            self.body[0].setpos(self.body[0].xcor() + MOVE_DISTANCE,self.body[0].ycor())

        elif self.body[0].heading() == LEFT:
            self.body[0].setpos(self.body[0].xcor() - MOVE_DISTANCE, self.body[0].ycor())

        elif self.body[0].heading() == UP:
            self.body[0].setpos(self.body[0].xcor(), self.body[0].ycor() + MOVE_DISTANCE)

        else:
            self.body[0].setpos(self.body[0].xcor(), self.body[0].ycor() - MOVE_DISTANCE)

        for i in range(0, len(self.body)):
            self.block[i] = self.body[i].pos()

    def eat(self):

        new_turtle = Turtle("square")
        new_turtle.penup()
        new_turtle.color("white")
        new_turtle.setpos(self.body[len(self.body)-1].pos())
        self.body.append(new_turtle)
        self.block.append(new_turtle.pos())





