from turtle import Screen, Turtle
import turtle

turtle.colormode(255)
t = Turtle()
s = Screen()
s.setup(height=500, width=700)
s.title("Microsoft Logo")
t.speed('slowest')

t.pu()
t.goto(-5, 0)
t.fillcolor((242, 80, 34))
t.color((242, 80, 34))
t.pd()
t.begin_fill()
for _ in range(4):
    t.left(90)
    t.forward(90)
t.end_fill()

t.pu()
t.goto(5, 0)
t.fillcolor((127, 186, 0))
t.color((127, 186, 0))
t.pd()
t.begin_fill()
for _ in range(4):
    t.forward(90)
    t.left(90)
t.end_fill()

t.pu()
t.goto(5, -10)
t.fillcolor((255, 185, 0))
t.color((255, 185, 0))
t.pd()
t.begin_fill()
for _ in range(4):
    t.forward(90)
    t.right(90)
t.end_fill()

t.pu()
t.goto(-5, -10)
t.fillcolor((0, 164, 239))
t.color((0, 164, 239))
t.pd()
t.begin_fill()
for _ in range(4):
    t.right(90)
    t.forward(90)
t.end_fill()
t.ht()
t.pu()
t.goto(0, -200)
t.color((115, 115, 115))
t.write(arg="Microsoft", move=False, align="center",
        font=("segoe", 40, "normal"))

s.exitonclick()
