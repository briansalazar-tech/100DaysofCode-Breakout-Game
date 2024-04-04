from turtle import Screen
from scoreboard import Walls, Scoreboard
from ball import Ball
from paddle import Paddle
from bricks import Row_1, Row_2, Row_3, Row_4, Row_5, Row_6, Row_7, Row_8
from time import sleep


def reset_ball_paddle():
    ball.reset_ball()
    paddle.reset_paddle()


def level_one():
    global large_bricks, medium_bricks
    row_1 = Row_1()
    row_2 = Row_2()
    row_3 = Row_3()
    large_bricks.append(row_1)
    large_bricks.append(row_3)
    medium_bricks.append(row_2)
    return


def level_two():
    global large_bricks, medium_bricks
    level_one()
    row_4 = Row_4()
    medium_bricks.append(row_4)
    return


def level_three():
    global large_bricks, medium_bricks
    level_one()
    level_two()
    row_5 = Row_5()
    large_bricks.append(row_5)
    return


def level_four():
    global large_bricks, medium_bricks
    level_one()
    level_two()
    level_three()
    row_6 = Row_6()
    medium_bricks.append(row_6)
    return


def level_five():
    global large_bricks, medium_bricks
    level_one()
    level_two()
    level_three()
    level_four()
    row_7 = Row_7()
    large_bricks.append(row_7)
    return


def level_six():
    global large_bricks, medium_bricks, small_bricks
    level_one()
    level_two()
    level_three()
    level_four()
    level_five()
    row_8 = Row_8()
    small_bricks.append(row_8)
    paddle.reset_paddle()
    ball.reset_ball()
    return


### GAME SETUP ###
## Brick Lists ##
large_bricks = []
medium_bricks = []
small_bricks = []

## Screen ##
gameboard = Screen()
gameboard.bgcolor("black")
gameboard.setup(width=1250, height=725)
gameboard.title("Breakout Game")
gameboard.tracer(0, 0)
gameboard.listen()

## Walls and Scoreboard ##
walls = Walls()
scoreboard = Scoreboard()
scoreboard.game_over_defeat()
scoreboard.update_scoreboard()

# Game Paddle ##
paddle = Paddle()
gameboard.onkeypress(paddle.go_left, key="Left")
gameboard.onkeypress(paddle.go_right, key="Right")
gameboard.onkeypress(reset_ball_paddle, key="r") # Reset Ball & Paddle

## Ball ##
ball = Ball()

### BREAK OUT GAME GAMEPLAY ###
gameboard.update()
sleep(1)
current_game = True
while current_game:
    sleep(ball.move_speed)
    gameboard.update()

    # If level == 7, game over
    if scoreboard.level == 7:
        scoreboard.game_over_win()
        current_game = False

    # If lives == 0, game over
    if scoreboard.lives == 0:
        scoreboard.game_over_defeat()
        current_game = False

    # Level 1 - Start
    if scoreboard.bricks == 0 and scoreboard.level == 0:
        level_one()
        scoreboard.level_up()
    
    # Level 2 - Start
    if scoreboard.bricks == 44 and scoreboard.level == 1:
        level_two()
        reset_ball_paddle()
        ball.move_speed -= 0.01
        scoreboard.level_up()
    
    # Level 3 - Start
    if scoreboard.bricks == 108 and scoreboard.level == 2:
        level_three()
        reset_ball_paddle()
        ball.move_speed -= 0.01
        scoreboard.level_up()
    
    # Level 4 - Start
    if scoreboard.bricks == 184 and scoreboard.level == 3:
        level_four()
        reset_ball_paddle()
        ball.move_speed -= 0.01
        scoreboard.level_up()
    
    # Level 5 - Start
    if scoreboard.bricks == 280 and scoreboard.level == 4:
        level_five()
        reset_ball_paddle()
        ball.move_speed -= 0.012
        scoreboard.level_up()
    
    # Level 6 - Start
    if scoreboard.bricks == 388 and scoreboard.level == 5:
        level_six()
        reset_ball_paddle()
        ball.move_speed -= 0.015
        print(ball.move_speed)
        scoreboard.level_up()
    
    # Game Over - Win
    if scoreboard.bricks == 554 and scoreboard.level == 6:
        reset_ball_paddle()
        scoreboard.level_up()

    # Ball hits large brick
    for row in large_bricks:
        for brick in row:
            if ball.distance(brick) < 55:
                brick.goto(1000,1000)
                ball.bounce_y()
                scoreboard.bricks_destroyed()
    
    # Ball hits medium brick
    for row in medium_bricks:
        for brick in row:
            if ball.distance(brick) < 41:
                brick.goto(1000,1000)
                ball.bounce_y()
                scoreboard.bricks_destroyed()
    
    # Ball hits small brick
    for row in small_bricks:
        for brick in row:
            if ball.distance(brick) < 30:
                brick.goto(1000,1000)
                ball.bounce_y()
                scoreboard.bricks_destroyed()

    # Ball hits left or right wall
    if ball.xcor() < -595 or ball.xcor() > 595:
        ball.bounce_x()

    # Ball hits cieling 
    if ball.ycor() > 340:
        ball.bounce_y()

    # Colision with paddle - paddle center
    if ball.distance(paddle) < 25 and ball.ycor() < -285:
        ball.bounce_y()

    # Colision with paddle - paddle edge
    if ball.distance(paddle) < 50 and ball.ycor() < -310:
        ball.bounce_edge()

    # Ball crosses floor - -1 Life
    if ball.ycor() < -362:
        reset_ball_paddle()
        scoreboard.life_lost()
    
    ball.move()

gameboard.exitonclick()