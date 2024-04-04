from turtle import Turtle

COLORS = ["#05B4FF", "#05FF82", "#1AFF05", "#FFFF05", "#FF9F05", "#FF7105", "#FE4646", "#FF0505"]

class SmallBrick(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)


class MediumBrick(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=2, stretch_len=3)


class LargeBrick(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=2, stretch_len=5)


# Row 1 - Large
def Row_1():
    large_start = -561
    row1 = []
    for brick in range(12):
        brick = LargeBrick()
        brick.color("black", COLORS[0])
        row1.append(brick)
    
    for brick in row1:
        brick.goto(large_start, 150)
        large_start += 102
    
    return row1


# Row 2 - Medium
def Row_2():
    medium_start = -581
    row2 = []
    for brick in range(20):
        brick = MediumBrick()
        brick.color("black", COLORS[1])
        row2.append(brick)
    
    for brick in row2:
        brick.goto(medium_start, 108)
        medium_start += 61

    return row2


# Row 3 - Large
def Row_3():
    large_start = -561
    row3 = []
    for brick in range(12):
        brick = LargeBrick()
        brick.color("black", COLORS[2])
        row3.append(brick)
    
    for brick in row3:
        brick.goto(large_start, 66)
        large_start += 102

    return row3


# Row 4 - Medium
def Row_4():
    medium_start = -581
    row4 = []
    for brick in range(20):
        brick = MediumBrick()
        brick.color("black", COLORS[3])
        row4.append(brick)
    
    for brick in row4:
        brick.goto(medium_start, 24)
        medium_start += 61

    return row4


# Row 5 - Large
def Row_5():
    large_start = -561
    row5 = []
    for brick in range(12):
        brick = LargeBrick()
        brick.color("black", COLORS[4])
        row5.append(brick)
    
    for brick in row5:
        brick.goto(large_start, -18)
        large_start += 102

    return row5


# Row 6 - Medium
def Row_6():
    medium_start = -581
    row6 = []
    for brick in range(20):
        brick = MediumBrick()
        brick.color("black", COLORS[5])
        row6.append(brick)
    
    for brick in row6:
        brick.goto(medium_start, -60)
        medium_start += 61

    return row6


# Row 7 Large
def Row_7():
    large_start = -561
    row7 = []
    for brick in range(12):
        brick = LargeBrick()
        brick.color("black", COLORS[6])
        row7.append(brick)
    
    for brick in row7:
        brick.goto(large_start, -102)
        large_start += 102

    return row7


# Row 8 Small
def Row_8():
    small_start = -600
    row8 = []
    for brick in range(58):
        brick = SmallBrick()
        brick.color("black", COLORS[7])
        row8.append(brick)
    
    for brick in row8:
        brick.goto(small_start, -134)
        small_start += 21

    return row8