from turtle import Turtle

class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len=5, stretch_wid=1, outline=0)
        self.penup()
        self.goto(0,-325)


    def go_left(self):
        if self.xcor() > -560:
            new_x = self.xcor() - 20
            self.goto(new_x, self.ycor())


    def go_right(self):
        if self.xcor() < 560:
            new_x = self.xcor() + 20
            self.goto(new_x, self.ycor())


    def reset_paddle(self):
        self.goto(0,-325)