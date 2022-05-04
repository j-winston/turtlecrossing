from turtle import Turtle, Screen
from car import Car
from scoreboard import Scoreboard
import time

# Setup screen dimensions
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
BACKGROUND_COLOR = 'black'

# Draw screen
screen = Screen()
screen.title('Turtle Crossing')
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor(BACKGROUND_COLOR)

# Game setup
game_on = True
# Turn off animation, use screen.update() instead
screen.tracer(0)

# Tracks level, game over and on screen messages
scoreboard = Scoreboard()

# Draw turtle
turtle = Turtle()
turtle.shape("turtle")
turtle.color("white")
turtle.penup()
turtle.setposition(0, -275)
turtle.setheading(90)


# Movement functions
def move_forward():
    turtle.forward(15)


# Listen for key events
screen.listen()
screen.onkeypress(move_forward, "Up")

# Automatically draws cars to screen
car = Car(num_cars=10)


# Main loop
while game_on:

    screen.update()
    # Moves all the random cars forward based on car.speed
    car.move_cars()

    # If turtle gets hit, end game and display GAME OVER
    if car.check_collision(turtle):
        game_on = False
        scoreboard.game_over()

    # Check if turtle made it across the street
    if turtle.ycor() > 360:
        scoreboard.print("You Made It!")
        scoreboard.change_level()
        time.sleep(1)
        turtle.setposition(0, -360)
        turtle.setheading(90)
        car.speed_up()


screen.exitonclick()