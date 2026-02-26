from turtle import *


#we want to paint a house

#step 1:draw a square
speed(10)
width(7)
color("red")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(70)
left(90)
begin_fill()
forward(80) #height of the door
right(90)
forward(70)
right(90)
forward(80)
end_fill()

penup()
goto(200, 200)
pendown()

begin_fill()
right(150)
forward(200)

left(120)
forward(200)
end_fill()

left (30)  
forward(40)
penup()
goto(30,160)
pendown()

begin_fill()
color("black")
forward(45)  #first window
left(90)
forward(45)
left(90)
forward(45)
left(90)
forward(45)
end_fill()



penup()
goto(170,160)
pendown()
begin_fill()
forward(45) #second window
left(90)
forward(45)
left(90)
forward(45)
left(90)
forward(45)
end_fill()


exitonclick()