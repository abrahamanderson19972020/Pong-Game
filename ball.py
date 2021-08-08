from turtle import Turtle


ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.shapesize(0.8, 0.8)
        self.penup()
        self.xmove = 10
        self.ymove = 10

    def move(self):
        x_coordinate = self.xcor() + self.xmove
        y_coordinate = self.ycor() + self.ymove
        self.goto(x_coordinate, y_coordinate)

    def bounce(self):
        self.ymove *= -1

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)


    def collision(self):
        self.xmove *= -1








