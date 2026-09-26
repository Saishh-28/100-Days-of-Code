from turtle import *
import time

# ---------------- SCREEN SETUP ---------------- #

screen = Screen()
screen.setup(width=800, height=600)

screen.bgcolor("black")
screen.title("PONG")

screen.tracer(0)

# ---------------- CENTRE LINE ---------------- #

line = Turtle()

line.color("white")

line.penup()

line.goto(0, 300)

line.setheading(270)

while line.ycor() > -300:

    line.pendown()
    line.forward(20)

    line.penup()
    line.forward(20)


# ---------------- PADDLE CLASS ---------------- #

class Paddle(Turtle):

    def __init__(self, position):

        super().__init__()

        self.shape("square")
        self.color("white")

        self.shapesize(stretch_wid=5, stretch_len=1)

        self.penup()
        self.goto(position)

    def up(self):

        new_y = self.ycor() + 8

        if new_y <= 250:
            self.goto(self.xcor(), new_y)

    def down(self):

        new_y = self.ycor() - 8

        if new_y >= -250:
            self.goto(self.xcor(), new_y)


# ---------------- BALL CLASS ---------------- #

class Ball(Turtle):

    def __init__(self):

        super().__init__()

        self.shape("circle")
        self.color("white")

        self.penup()
        self.goto(0, 0)

        self.x_move = 4
        self.y_move = 4

    def move(self):

        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move

        self.goto(new_x, new_y)

    def bounce_y(self):

        self.y_move *= -1

    def bounce_x(self):

        self.x_move *= -1

    def reset_ball(self):

        self.goto(0, 0)

        self.bounce_x()


# ---------------- SCOREBOARD CLASS ---------------- #

class Scoreboard(Turtle):

    def __init__(self):

        super().__init__()

        self.color("white")

        self.penup()
        self.hideturtle()

        self.goto(0, 260)

        self.left_score = 0
        self.right_score = 0

        self.update_score()

    def update_score(self):

        self.clear()

        self.write(
            f"{self.left_score}    {self.right_score}",
            align="center",
            font=("Courier", 24, "normal")
        )

    def left_point(self):

        self.left_score += 1
        self.update_score()

    def right_point(self):

        self.right_score += 1
        self.update_score()


# ---------------- OBJECT CREATION ---------------- #

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

ball = Ball()

scoreboard = Scoreboard()


# ---------------- MOVEMENT FLAGS ---------------- #

right_up = False
right_down = False

left_up = False
left_down = False


# ---------------- MOVEMENT FUNCTIONS ---------------- #

def right_paddle_up():

    global right_up
    right_up = True


def right_paddle_down():

    global right_down
    right_down = True


def left_paddle_up():

    global left_up
    left_up = True


def left_paddle_down():

    global left_down
    left_down = True


# ---------------- STOP FUNCTIONS ---------------- #

def stop_right_up():

    global right_up
    right_up = False


def stop_right_down():

    global right_down
    right_down = False


def stop_left_up():

    global left_up
    left_up = False


def stop_left_down():

    global left_down
    left_down = False


# ---------------- KEYBOARD CONTROLS ---------------- #

screen.listen()

screen.onkeypress(right_paddle_up, "Up")
screen.onkeyrelease(stop_right_up, "Up")

screen.onkeypress(right_paddle_down, "Down")
screen.onkeyrelease(stop_right_down, "Down")

screen.onkeypress(left_paddle_up, "w")
screen.onkeyrelease(stop_left_up, "w")

screen.onkeypress(left_paddle_down, "s")
screen.onkeyrelease(stop_left_down, "s")


# ---------------- GAME LOOP ---------------- #

game_is_on = True

while game_is_on:

    time.sleep(0.01)

    screen.update()

    ball.move()

    # SMOOTH PADDLE MOVEMENT

    if right_up:
        right_paddle.up()

    if right_down:
        right_paddle.down()

    if left_up:
        left_paddle.up()

    if left_down:
        left_paddle.down()

    # WALL COLLISION

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # RIGHT PADDLE COLLISION

    if (
        ball.distance(right_paddle) < 50
        and ball.xcor() > 320
    ):
        ball.bounce_x()

    # LEFT PADDLE COLLISION

    if (
        ball.distance(left_paddle) < 50
        and ball.xcor() < -320
    ):
        ball.bounce_x()

    # RIGHT WALL MISSED

    if ball.xcor() > 390:

        scoreboard.left_point()

        ball.reset_ball()

    # LEFT WALL MISSED

    if ball.xcor() < -390:

        scoreboard.right_point()

        ball.reset_ball()


screen.mainloop()