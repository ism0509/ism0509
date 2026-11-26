import turtle
import time

turtle.shape('turtle')
turtle.speed(0)

length = 10


for i in range(15):
    for colors in ['white', 'snow', 'ghost white', 'snow2', 'light gray', 'gainsboro', 'gray', 'snow3', 'snow4', 'slate gray']:
        turtle.color(colors)
        turtle.pendown()
        turtle.begin_fill()
        for i in range(7):
            turtle.forward(length)
            turtle.right(360/7)
        turtle.end_fill()
        turtle.penup()
        turtle.left(60)
        turtle.forward(length)
        length += 5

time.sleep(100)