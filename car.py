from turtle import Turtle
import random
import time


class Car(Turtle):
    def __init__(self, num_cars):
        super().__init__()
        self.penup()
        self.shape('square')
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.hideturtle()
        self.num_cars = 10
        self.cars = []
        self.speed = .07
        self.draw_cars()

    def draw_cars(self):

        # Assign 8 random colored cars to an array
        for _ in range(self.num_cars):
            # Set car attributes
            car = Turtle()
            car.penup()
            car.shape('square')
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.hideturtle()
            color_palette = ['red', 'yellow', 'green', 'blue', 'orange', 'purple', 'gray']
            car_color = random.choice(color_palette)
            car.color(car_color)
            # Set initial positions to off-screen
            x_loc = random.randint(400, 1000)
            y_loc = random.randint(-245, 250)
            car.setheading(180)
            car.setposition(x_loc, y_loc)
            car.showturtle()
            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.forward(self.speed)
            # As a car leaves the screen, generate a new one off-screen at a new location
            if car.xcor() < -400:
                x_loc = random.randint(300, 800)
                y_loc = random.randint(-250, 250)
                car.setposition(x_loc, y_loc)

    def check_collision(self, turtle):
        for car in self.cars:
            if car.distance(turtle) < 30:
                return True

    def speed_up(self):
        self.speed += .05
