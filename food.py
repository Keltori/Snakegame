from turtle import Turtle, Screen
import random
import time

screen = Screen()
screen.tracer(0)
GRID = []
BLOCKED = [(-40, 0), (-20, 0), (0, 0)]
for i in range(-14, 15):
    for j in range(-14, 15):
        GRID.append((20 * i, 20 * j))


class Food(Turtle):
    def __init__(self):
        super(Food, self).__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("green")
        self.relocate(BLOCKED)

    def relocate(self, blocked):
        time.sleep(0.1)
        self.clear()
        GRID = []
        for i in range(-14, 15):
            for j in range(-14, 15):
                GRID.append((20 * i, 20 * j))
        for block in blocked:
            GRID.remove(block)
        self.setpos(random.choice(GRID))
        screen.update()