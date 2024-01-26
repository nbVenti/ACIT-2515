import random
from turtle import *
setup()
t1 = Turtle()

t1.up()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
t1.speed(1)
while True:
    x = random.randint(-350, 350)
    y = random.randint(-350, 350)
    circle_size = random.randint(10, 100)
    circle_color = random.choice(colors)
    t1.goto(x, y)
    t1.down()
    t1.color(circle_color)
    t1.circle(circle_size)
    t1.up()