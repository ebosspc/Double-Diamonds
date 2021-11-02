#Program to draw peaks

#Import turtle libary for drawing
import turtle as trtl

#Set initial conditions for painter object
painter = trtl.Turtle()
painter.penup()
painter.pensize(3)
painter.speed(0)
painter.goto(-200, 0)
painter.pendown()

#Set initial postions and movement values
x = -200
y = 0
move_x = 1
move_y = 1

#While loop that will repeat itself twice
while (x < 200):
  #This nested while loop will draw the first line moving up
  while (y < 100):
    x = x + move_x
    y = y + move_y
    painter.goto(x,y)
  move_y = -1
  
  #This next while loop will draw the next line moving down
  while (y > 0):
    x = x + move_x
    y = y + move_y
    painter.goto(x,y)
  move_y = 1  
#Reset for next loop that will mirror the image
x = -200
y = 0
move_x = 1
move_y = -1
painter.penup()
painter.goto(x,y)
painter.pendown()

#Mirror image of first nested while loop, and it will repeat itself twice
while(x < 200):

  #This nested while loop will draw the first line moving down 
  while (y > -100):
    x = x + move_x
    y = y + move_y
    painter.goto(x,y)
  move_y = 1
  
  #This next while loop will draw the next line moving up
  while (y < 0):
    x = x + move_x
    y = y + move_y
    painter.goto(x,y)
  move_y = -1


wn = trtl.Screen()
wn.mainloop()