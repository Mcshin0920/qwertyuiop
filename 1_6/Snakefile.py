#   a116_buggy_image.py

import turtle as trtl
from typing import Counter

# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
# Create a spider body

spider = trtl.Turtle()
spider.pensize(40)
spider.circle(20)
leg = 6


# Configure spider legs
'''y = 70'''
# y is how long the legs are

length = 70
number = 380 / leg
spider.pensize(5)
counter = 0

# Draw legs

while (counter < leg):
  spider.goto(0,0)
  spider.setheading(number*counter)
  spider.forward(length)
  counter = counter + 1
spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()