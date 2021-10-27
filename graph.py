import turtle


def grid(totallength, yval, yint):
    space = turtle.Screen()
    p = turtle.Turtle()
    repeating = int(totallength/10)
    space.setup(500, 500)

    p.speed(0)
    p.penup()
    p.goto(-totallength, -totallength)
    p.pendown()
    x = -totallength
    y = -totallength

    for i in range(repeating*2):     
        p.goto(-x, y)
        y = y + 10
        p.penup()
        p.goto(-x, y)
        p.pendown()
        p.goto(x, y)

    p.penup()
    p.goto(-totallength, -totallength)
    p.pendown()
    x = totallength
    y = totallength

    for i in range(repeating*2):     
        p.goto(-x, y)
        x = x - 10
        p.penup()
        p.goto(-x, y)
        p.pendown()
        p.goto(-x, -y)

    p.penup()
    p.goto(0, -y)
    p.pensize(5)
    p.pendown()
    p.goto(0, y)

    p.penup()
    p.goto(-x, 0)
    p.pensize(5)
    p.pendown()
    p.goto(x, 0)

    yint = yint* 10

    linear(p, yval, yint, totallength)

    


    space.mainloop()

def linear(turtle, y, intercept, screensize):
    turtle.pencolor("blue")
    turtle.pensize(2)
    turtle.penup()
    turtle.goto(0, intercept)
    turtle.pendown()
    turtle.setheading(turtle.towards(100, y))
    turtle.forward(screensize)
    turtle.stamp()
    turtle.left(180)
    turtle.forward(screensize * 2)
    turtle.stamp()