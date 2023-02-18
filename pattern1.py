from turtle import *
import random
colors = ["yellow","red","green","blue","pink","cyan"]
bgcolor("black")
speed(9)
pensize(2)

begin_fill()
posForward = 200
posAngle = 70

while True:
    pencolor(colors[random.randint(0,5)])
    forward(posForward)
    left(posAngle)
    back(posAngle)
    right(posForward)
    circle(80)
    if(abs(pos()) < 10):
        break

end_fill()
done()
