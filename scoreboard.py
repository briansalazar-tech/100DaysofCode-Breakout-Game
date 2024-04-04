from turtle import Turtle

class Scoreboard(Turtle):    

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.level = 0
        self.bricks = 0
        self.lives = 3
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.color("white")
        self.goto(-525, 300)
        self.write(f"Level: {self.level}", align="center", font=("Courier",20, "bold"))
        self.goto(-250, 300)
        self.write(f"Bricks Destroyed: {self.bricks}", align="center", font=("Courier",20, "bold"))
        self.goto(520, 300)
        self.write(f"Lives: {self.lives}", align="center", font=("Courier",20, "bold"))


    def level_up(self):
        if self.level != 7:
            self.level += 1
            self.update_scoreboard()


    def bricks_destroyed(self):
        self.bricks += 1
        self.update_scoreboard()


    def life_lost(self):
        if self.lives != 0:
            self.lives -= 1
            self.update_scoreboard()


    def game_over_win(self):
        self.color("#BBFFA0")
        self.goto(0, 0)
        self.write("You win!!", align="center", font=("Arial",50, "bold"))
        self.goto(0, -50)
        self.color("grey")
        self.write("Click the screen to exit.", align="center", font=("Arial",20, "bold"))


    def game_over_defeat(self):
        self.color("red")
        self.goto(0, 0)
        self.write("Game Over...", align="center", font=("Arial",50, "bold"))
        self.goto(0, -50)
        self.color("grey")
        self.write("Click the screen to exit.", align="center", font=("Arial",20, "bold"))
        

class Walls(Turtle):

    def __init__(self):
        super().__init__()
        self.color("grey")
        self.penup()
        self.hideturtle()
        self.goto(-617,-355)
        self.pendown()
        self.pensize(12)
        self.left(90)
        self.forward(712) # Left wall
        self.right(90)
        self.forward(1233) # Top wall
        self.right(90)
        self.forward(715) # Right wall
