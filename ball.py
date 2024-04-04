from turtle import Turtle
from time import sleep
from random import randint

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.oldx = 0
        self.oldy = 0
        self.xdir = ""
        self.ydir = ""
        self.wide_neg = 1
        self.wide_pos = 1
        
        self.setheading(randint(45, 135))
        self.goto(0, -295)
        self.move_speed = 0.06

    
    def move(self):
        self.forward(10)
        if self.xcor() > self.oldx:
            self.xdir = "Positive"
            self.oldx = self.xcor()
        elif self.xcor() < self.oldx:
            self.xdir = "Negative"
            self.oldx = self.xcor()

        if self.ycor() > self.oldy:
            self.ydir = "Positive"
            self.oldy = self.ycor()
        elif self.ycor() < self.oldy:
            self.ydir = "Negative"
            self.oldy = self.ycor()
        
    
    def bounce_y(self): # Top wall & Bottom bricks / Paddle Center & Top bricks
        
        if self.xdir == "Positive" and self.ydir == "Positive":
            self.sety(self.ycor() - 10)
            self.setheading(self.heading() - 90)

        if self.xdir == "Negative" and self.ydir == "Positive":
            self.sety(self.ycor() - 10)
            self.setheading(self.heading() + 90)

        if self.xdir == "Positive" and self.ydir == "Negative":
            self.sety(self.ycor() + 10)
            self.setheading(self.heading() + 90)
            
        if self.xdir == "Negative" and self.ydir == "Negative":
            self.sety(self.ycor() + 10)
            self.setheading(self.heading() - 90)

 
    def bounce_x(self): # Left wall/ Right wall
        
        if self.xdir == "Negative" and self.ydir == "Negative":
            self.setx(self.xcor() + 10)
            self.setheading(self.heading() + 90)

        if self.xdir == "Negative" and self.ydir == "Positive":
            self.setx(self.xcor() + 10)
            self.setheading(self.heading() - 90)

        if self.xdir == "Positive" and self.ydir == "Positive":
            self.setx(self.xcor() - 10)
            self.setheading(self.heading() + 90)

        if self.xdir == "Positive" and self.ydir == "Negative":
            self.setx(self.xcor() - 10)
            self.setheading(self.heading() - 90)

    
    def bounce_edge(self): # Paddle Edges
        # wide_pos and wide_neg variables ensure bounce andle is not just 90 degrees
        if self.xdir == "Positive" and self.ydir == "Negative":
            self.sety(self.ycor() + 8)
            
            if self.wide_pos == 1:
                self.setheading(self.heading() + 70) # 70 makes obtuce bounce. However, on second call, bounces into floor
                self.wide_pos = 0
            
            if self.wide_pos == 0:
                self.setheading(self.heading() + 30) # Alternate with acute angle to prevent from boucing into floor
                self.wide_pos = 1

        if self.xdir == "Negative" and self.ydir == "Negative":
            self.sety(self.ycor() + 8)
            
            if self.wide_neg == 1:
                self.setheading(self.heading() - 70)
                self.wide_neg = 0
            
            if self.wide_neg == 0:
                self.setheading(self.heading() - 30)
                self.wide_neg = 1


    def reset_ball(self):
        self.goto(0, -298)
        self.setheading(randint(45, 135))
        sleep(0.09)