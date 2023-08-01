import random
import turtle
from turtle import Turtle, Screen


def random_rgb():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    rgb_tuple = (r, g, b)
    return rgb_tuple


def triangle():
    for _ in range(5):
        t.right(120)
        t.forward(400)


t = Turtle()
turtle.colormode(255)
t.speed("fastest")
s = Screen()
s.title("Spiral Pattern")
s.bgcolor("black")


def print_spiral_triangle(gape):
    t.ht()
    for i in range(int(360 / gape)):
        t.pencolor(random_rgb())
        triangle()
        t.setheading(t.heading() + gape)


t.pu()
t.goto(x=200, y=100)
t.pd()
print_spiral_triangle(4)

turtle.done()
