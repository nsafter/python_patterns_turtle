from turtle import *
import random

goto(0,-200)
pensize(2)
left(90)
bgcolor("black")
pencolor("brown")
speed("fastest")
#backward(100)
colormode(255)

def tree(i):
    if(i<15):
        return
    
    else:
        forward(i)
        color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        circle(3)
        color("brown")
        left(30)
        tree(3*i/4)
        right(60)
        tree(3*i/4)
        left(30)
        backward(i)

n = 150
#setpos(0,-n)
tree(n)
done()
