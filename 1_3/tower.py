#   a113_tower.py
#   Modify this code in VS Code to alternate the colors of the 
#   floors every three floors
import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)
painter.pensize(5)

# starting location of the tower


# height of tower and a counter for each floor
num_floors = 63
floor = 0


def towers(color1, color2, color3, floors):
  x = -150
  y = -150
  z = -150
  c = -150
  painter.penup()
  painter.goto(x, y)
  painter.color(color1)
  y = y + 5 
  col = floors % 3
  if (col == 2):
    painter.color(color2)
  if (col == 1):
    painter.color(color3)
  floors = floors + 1
   
    #draw the floor
  painter.pendown()
  painter.forward(50)


while floor < num_floors:
  #building one
  if (floor < 21):
    towers("gray", "blue", "green", floor)

  #building two
  elif(floor < 42):
    painter.penup()
    painter.goto(-250, z)
    painter.color("gray")
    z = z + 5 # location of next floor
    col = floor % 3
    if (col == 2):
      painter.color("yellow")
    if (col == 1):
      painter.color("green")
    floor = floor + 1
   
    #draw the floor
    painter.pendown()
    painter.forward(50)
  
  #building three
  else:
    painter.penup()
    painter.goto(-50, c)
    painter.color("gray")
    c = c + 5 # location of next floor
    col = floor % 3
    if (col == 2):
      painter.color("red")
    if (col == 1):
      painter.color("brown")
    floor = floor + 1
   
    painter.pendown()
    painter.forward(50)



wn = trtl.Screen()
wn.mainloop()