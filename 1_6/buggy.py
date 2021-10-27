#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used

p = trtl.Turtle()
p.pensize(40)
p.circle(20)
p.pensize(5)

x = 6
y = 70
z = 380 / x

value = 0

while (value < x):
  p.goto(0,0)
  p.setheading(z*value)
  p.forward(y)
  value = value + 1
  


p.hideturtle()
wn = trtl.Screen()
wn.mainloop()