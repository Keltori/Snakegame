from turtle import Turtle,Screen
screen = Screen()


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.hideturtle()
        self.pencolor("white")
        self.penup()
    def score(self,current):
        self.clear()
        self.setpos(0, 325)
        self.pendown()
        self.write(f"Score: {current}", False, align="center", font=["Arial", 40, "normal"])

    def wall(self):
        self.setpos(290, 290)
        self.pendown()
        self.goto(290, -290)
        self.goto(-290, -290)
        self.goto(-290, 290)
        self.goto(290, 290)
        self.penup()

    def highscore(self,current_high_score):
        self.clear()
        self.setpos(0, -350)
        self.pendown()
        self.write(f"Highscore: {current_high_score}", False, align="center", font=["Arial", 40, "normal"])

    def gameover(self):
        self.penup()
        self.goto(0,0)
        self.color("Red")
        self.pendown()
        self.write("GAME OVER!", False, align="center", font=["Arial", 40, "normal"])
        screen.update()