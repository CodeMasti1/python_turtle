import random
import turtle
from turtle import Turtle, Screen


def random_rgb():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    rgb_tuple = (r, g, b)
    return rgb_tuple


t = Turtle()
turtle.colormode(255)
t.speed("fastest")

s = Screen()
s.title("Spiral Pattern")
s.bgcolor("black")


def print_spiral_circle(gape):
    t.ht()
    for i in range(int(360 / gape)):
        t.pencolor(random_rgb())
        t.circle(100)
        t.setheading(t.heading() + gape)


print_spiral_circle(8)

turtle.done()
