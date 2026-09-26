# from turtle import *
# import random

# Tim = Turtle()
# Tim.color("salmon")
# Tim.shape("turtle")
# Tim.pensize(5)
# Tim.speed(0)
# screen = Screen()
# screen.colormode(255)
# for i in range(15):
#     Tim.pendown()
#     Tim.forward(10)
#     Tim.penup()
#     Tim.forward(10)

# def drawShape(numOfSides):
#     angle = 360/numOfSides
#     for i in range(numOfSides):
#         Tim.color((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
#         Tim.forward(80)
#         Tim.right(angle)

# colours = ["sandy brown", "orange", "dark orange", "chocolate", "firebrick", "brown", "dark red", "maroon"]

# for i in range(3,10):
#     drawShape(i)

# X_BOUND = 350
# Y_BOUND = 350    
# directions = ["right", "left", "forward", "backward"]
# while True:
#     pick = random.choice(directions)
#     Tim.color((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
#     if pick == "right": 
#         Tim.right(90)
#     elif pick == "left":
#         Tim.left(90)
#     elif pick == "forward":
#         Tim.forward(20)
#     elif pick =="backward":
#         Tim.back(20)
#     Tim.forward(20)
#         # 2. Get current position
#     x, y = Tim.xcor(), Tim.ycor()
    
#     # 3. Check boundaries and teleport/turn back if outside
#     if abs(x) > X_BOUND or abs(y) > Y_BOUND:
#         Tim.undo()  # Undo the last step
#         Tim.left(180)  # Turn around
# def spirography(gap):
#     heading = Tim.heading()
#     for i in range(int(360/gap)):
#         Tim.color((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
#         Tim.circle(100)
#         heading += gap
#         Tim.setheading(heading)


# spirography(5)

# hirst_palette = [
#     # --- Pastel & Creamy Tones ---
#     (240, 192, 192),  # Soft Rose Pink
#     (245, 215, 170),  # Creamy Apricot
#     (220, 235, 200),  # Pale Pistachio
#     (200, 225, 240),  # Soft Powder Blue
#     (230, 210, 240),  # Gentle Lavender
#     (255, 235, 180),  # Mellow Butter Yellow
    
#     # --- Vibrant Mid-Century Pop ---
#     (235, 90, 100),   # Hirst Coral Red
#     (245, 130, 70),   # Bright Marigold Orange
#     (250, 200, 50),   # Mustard Gold
#     (80, 185, 140),   # Minty Emerald
#     (70, 160, 210),   # Cerulean Blue
#     (160, 110, 200),  # Retro Purple
    
#     # --- Deep & Rich Earthy Tones ---
#     (180, 60, 80),    # Terracotta Berry
#     (200, 100, 60),   # Burnt Copper
#     (160, 140, 80),   # Olive Khaki
#     (50, 120, 110),   # Deep Teal
#     (60, 90, 140),    # Classic Navy Accent
#     (110, 70, 120),   # Deep Plum
    
#     # --- Bright Neon Pops (For Contrast) ---
#     (255, 110, 160),  # Bubblegum Pink
#     (255, 170, 50),   # Tangerine Dream
#     (180, 230, 60),   # Lime Electric
#     (40, 210, 200),   # Vivid Turquoise
#     (130, 90, 255),   # Neon Violet
#     (255, 90, 130),   # Hot Punch
    
#     # --- Muted Retro & Sage ---
#     (200, 160, 150),  # Dusty Mauve
#     (170, 180, 150),  # Sage Green
#     (150, 170, 180),  # Steel Blue
#     (190, 150, 170),  # Antique Rose
#     (215, 190, 160),  # Warm Sand
#     (140, 160, 140)   # Eucalyptus Green
# ]
# Tim.penup()
# Tim.setheading(210)
# Tim.forward(350)
# Tim.setheading(0)

# for j in range(10):
    
#     for i in range(12):
#         Tim.dot(20, random.choice(hirst_palette))
#         Tim.forward(50)
    

#     Tim.setheading(180)
#     Tim.forward(50 * 12)  
#     Tim.setheading(90)
#     Tim.forward(50)
#     Tim.setheading(0)
        

# screen.exitonclick()

        


# def north():
#     Tim.forward(10)
# def south():
#     Tim.back(10)
# def east():
#     Tim.right(25)
# def west():
#     Tim.left(25)
# def clear():
#     Tim.penup()
#     Tim.clear()
#     Tim.home()
#     Tim.pendown()



# screen.onkey(north, "w")
# screen.onkey(south, "s")
# screen.onkey(east, "d")
# screen.onkey(west, "a")
# screen.onkey(clear, "c")
# screen.listen()

#bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter colour: ")
# print(bet)

# race = False
# colours = ["red","orange", "yellow", "green", "blue", "purple"]
# space = 0
# turts = []
# for colour in colours:
#     new_turtle = Turtle(shape="turtle")
#     new_turtle.penup()
#     new_turtle.color(colour)
#     new_turtle.goto(-230,-120+space)
#     space += 50
#     turts.append(new_turtle)

# if bet:
#     race = True

# x = -230
# while race:
#     for turt in turts:
#         if turt.xcor() >= 230:
#             if turt.color() == bet:
#                 print("you won")
#             else:
#                 winner_turt_colour = turt.pencolor()
#                 print( winner_turt_colour, "turtle won, you lost")
#             race = False
#         ahead = random.randint(0,10)
#         turt.forward(ahead)
# new_turtle.speed(0)
# new_turtle.pensize(3)