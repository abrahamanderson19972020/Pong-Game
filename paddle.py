from turtle import Turtle


class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.position = position
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(5, 1)
        self.setposition(self.position)


    def up(self):
        y_coordinate = self.ycor() + 40
        self.goto(self.xcor(), y_coordinate)


    def down(self):
        y_coordinate = self.ycor() - 40
        self.goto(self.xcor(), y_coordinate)



