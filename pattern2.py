from turtle import *
import random
pensize(2)
bgcolor("black")
pencolor("white")
speed("normal")
colormode(255)
begin_fill()
length = 10
angle = 91
for i in range(150):
    pencolor(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    forward(length)
    right(angle)
    length += 3 

end_fill()
done()
