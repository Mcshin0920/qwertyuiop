#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []
my_colors = []
# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  my_turtles.append(t)
  my_colors.append(t)

#  
startx = 0
starty = 0

#
x = 50
for t in my_turtles:
  t.forward(x)
  t.right(45)     
  x = x + 50

wn = trtl.Screen()
wn.mainloop()