from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")


class Score(Turtle):
    def __init__(self,position,username):
        super().__init__()
        self.position = position
        self.username = username
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(self.position)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"{self.username}: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()