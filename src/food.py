from turtle import Turtle
import random
import math

def get_location():
        result = random.randint(-270, 270)
        result = math.ceil(result / 20) * 20
        return result

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(1)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.goto(get_location(), get_location())