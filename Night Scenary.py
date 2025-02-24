from turtle import *
import random

Screen().tracer(100)
speed(900000)
hideturtle()
bgcolor("#0B0B45")

#Stars
def stars(x, y, size=2):
    speed(100)
    penup()
    goto(x,y)
    pendown()
    dot(size,"white")


for i in range(100):
    x = random.randint(-1000, 1000)
    y = random.randint(-700, 700)
    stars(x, y, random.randint(2,5))

#Moon
penup()
goto(-50, -50)
color("#e6edf7")
begin_fill()
circle(200)
end_fill()

#Dots
penup()
goto(-150, 150)
color("#cfd7e3")
begin_fill()
circle(65)
end_fill()

penup()
goto(-130, 50)
color("#cfd7e3")
begin_fill()
circle(45)
end_fill()

penup()
goto(-90, 0)
color("#d3dded")
begin_fill()
circle(25)
end_fill()

penup()
goto(50, 200)
color("#d3dded")
begin_fill()
circle(15)
end_fill()


#River
color("#182078")
begin_fill()
penup()
goto(-1000, -190)
pendown()
for d in range(4):
    forward(2000)
    right(90)
    forward(200)
end_fill()



#mountain
def mount(d, u):
    penup()
    goto(d, u)
    pendown()
mount(-800, -200)

color("#2C3930")
begin_fill()
fd(600)
lt(150)
fd(1000)
lt(180-120)
fd(1000)
lt(150)
fd(600)
end_fill()

mount(-800, -200)
color("#1A1A19")
begin_fill()
fd(700)
lt(144)
fd(700)
lt(180-108)
fd(700)
lt(144)
fd(800)
end_fill()

#mount 2
mount(1100, -200)
color("#2C3930")
begin_fill()
fd(600)
lt(150)
fd(1000)
lt(180-120)
fd(1000)
lt(150)
fd(600)
end_fill()

mount(400, -200)
color("#1A1A19")
begin_fill()
fd(700)
lt(144)
fd(700)
lt(180-108)
fd(700)
lt(144)
fd(800)
end_fill()

#river 2
def lines(x, y):
    color("white")
    speed(100)
    penup()
    goto(x,y)
    pendown()
    forward(100)

for p in range(10):
    x = random.randint(-1000, 1000)
    y = random.randint(-700, -200)
    lines(x, y)

#Trees
def tree(a, b, c, d, e, f):
    pu()
    goto(a, b)
    pd()
    color("black")
    begin_fill()
    forward(30)
    setheading(120)
    forward(30)
    setheading(240)
    forward(30)
    setheading(270)
    end_fill()
    
    penup()
    goto(c, d)
    forward(60)
    pendown()
    begin_fill()
    setheading(0)
    forward(30)
    setheading(120)
    forward(30)
    setheading(240)
    forward(30)
    setheading(270)
    end_fill()
    #wood
    penup()
    goto(e,f)
    setheading(0)
    forward(40)
    pendown()
    begin_fill()
    color("black")
    setheading(270)
    forward(40)
    setheading(0)
    forward(5)
    setheading(90)
    forward(40)
    end_fill()

#left

tree(-800, -140, -800, -100,-828, -158)
setheading(0)
tree(-700, -140, -700, -100,-727, -158)
setheading(0)
tree(-600, -140, -600, -100,-626, -158)
setheading(0)
tree(-500, -140, -500, -100,-528, -158)
setheading(0)
tree(-400, -140, -400, -100,-428, -158)
setheading(0)
tree(-300, -140, -300, -100,-328, -158)

Screen().update()
done()