import turtle
b=turtle.Turtle()
b.color('red')
b.circle(50)
c=100
d=['red','green','blue','orange','black']
for i in range(0,5):
    b.penup()
    b.goto(c,100)
    b.pendown()
    b.color(d[i])
    b.circle(70)
    c=c-10
b.penup()
b.goto(200,200)
b.pendown()
for i in range(5):
    b.forward(100)
    b.right(144)
b.penup()
b.goto(-200,200)
b.pendown()
for i in range(0,4):
    b.forward(100)
    b.right(90)
b.penup()
b.goto(200,125)
b.pendown()
b.fd(200)
    
