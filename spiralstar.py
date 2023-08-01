import random
import turtle
from turtle import Turtle, Screen


def random_rgb():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    rgb_tuple = (r, g, b)
    return rgb_tuple


def star():
    for _ in range(5):
        t.right(144)
        t.forward(200)


t = Turtle()
turtle.colormode(255)
t.speed("fast")
s = Screen()
s.title("Spiral Pattern")
s.bgcolor("black")


def print_spiral_star(gape):
    t.ht()
    for i in range(int(360 / gape)):
        t.pencolor(random_rgb())
        star()
        t.setheading(t.heading() + gape)


print_spiral_star(10)

turtle.done()
