from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.allCars = []

    def create_car(self):
        random_number = random.randint(1 , 6)
        if random_number == 1:
            car = Turtle("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.color(random.choice(COLORS))
            y_position = random.randint(-250, 250)
            car.goto(300, y_position)
            self.allCars.append(car)

    def move_cars(self):
        for car in self.allCars:
            car.backward(STARTING_MOVE_DISTANCE)

