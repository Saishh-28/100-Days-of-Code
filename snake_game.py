from turtle import *
import random
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("The Snake Game.")
screen.tracer(0)
screen.colormode(255)
start = screen.textinput("Welcome!","Start Game?: Y/N")
while True:
    if start == "Y":
        game = True
        break
    else:
        start = screen.textinput("Start Game?: Y/N")


class Snake:
    def __init__(self):
        self.__turts = []
        self.snakeBody() 
        self.points = 0
        
    def snakeBody(self):
        ahead = 0
        for i in range(3): 
            snake = Turtle(shape="square")
            snake.color((random.randint(50,255), random.randint(50,255), random.randint(50,255)))
            snake.penup()
            snake.forward(ahead)
            ahead -= 20
            self.__turts.append(snake)
        screen.update()

    def get_head(self):
        return self.__turts[0]

    def addSegment(self):
        new_segment = Turtle(shape="square")
        new_segment.color((random.randint(50,255), random.randint(50,255), random.randint(50,255)))
        new_segment.penup()
        
        last_x = self.__turts[-1].xcor()
        last_y = self.__turts[-1].ycor()
        new_segment.goto(last_x, last_y)
        
        self.__turts.append(new_segment)

    def Move(self):
        for turt_index in range(len(self.__turts) - 1, 0, -1):
            new_x = self.__turts[turt_index - 1].xcor()
            new_y = self.__turts[turt_index - 1].ycor()
            self.__turts[turt_index].goto(new_x, new_y)
        self.__turts[0].forward(20)
    
    def GetPosition(self):
        pos = []
        for segments in self.__turts:
            pos.append((round(segments.xcor()), round(segments.ycor())))
        return pos

    def north(self):
        if self.__turts[0].heading() != 270: 
            self.__turts[0].setheading(90)
            
    def south(self):
        if self.__turts[0].heading() != 90:
            self.__turts[0].setheading(270)
            
    def east(self):
        if self.__turts[0].heading() != 180:
            self.__turts[0].setheading(0)
            
    def west(self):
        if self.__turts[0].heading() != 0:
            self.__turts[0].setheading(180)
        
    def restart(self):
        for turt in self.__turts:
            turt.hideturtle() # Makes the physical body disappear
        self.__turts.clear() # Wipes the array completely empty
        self.points = 0      # Resets your scoreboard point score
        clear()              # Wipes the "YOU LOST" text off screen
        self.snakeBody()     # Rebuilds a fresh 3-segment snake


class Food(Turtle):
    def __init__(self, shape = "circle", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.penup()
        self.shapesize(0.5, 0.5) 
        self.color("yellow")
        self.speed(0)
        self.Move()

    def Move(self):
        new_x = random.randint(-13, 13) * 20
        new_y = random.randint(-13, 13) * 20
        self.goto(new_x, new_y)


# --- Initialize Objects ---
my_snake = Snake()
my_food = Food()

screen.listen()
screen.onkey(my_snake.north, "Up")
screen.onkey(my_snake.south, "Down")
screen.onkey(my_snake.east, "Right")
screen.onkey(my_snake.west, "Left")




while game:
    screen.update()
    time.sleep(0.1) 
    my_snake.Move()
    
    # Food collision
    if my_snake.get_head().distance(my_food) < 15:
        my_food.Move()
        my_snake.addSegment()
        my_snake.points += 1
        
        # Win Condition
        if my_snake.points == 10:
            # ADDED: Changes text color to green and writes in the center
            color("green")
            write("YOU WON!", align="center", font=("Courier", 36, "bold"))
            game = False
            
    # Self-collision check
    snake_positions = my_snake.GetPosition()
    if snake_positions[0] in snake_positions[2:]:
        # ADDED: Changes text color to red and writes in the center
        color("red")
        write("YOU LOST", align="center", font=("Courier", 36, "bold"))
        game = False
        
    # Wall collision check
    head = my_snake.get_head()
    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
        color("red")
        write("YOU LOST", align="center", font=("Courier", 36, "bold"))
        game = False
    
    if not game:
        trying = screen.textinput("Uh oh!","Retry Game?: Y/N")
        if trying == "Y":
            game = True
            my_snake.restart()
            screen.listen()



screen.update()
screen.exitonclick()
