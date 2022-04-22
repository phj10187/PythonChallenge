#060
import turtle
turtle.shape("turtle")

for i in range(0,4):
  turtle.forward(50)
  turtle.right(90)
  
  turtle.exitonclick()
#061
import turtle
turtle.shape("turtle")

for i in range(0,3):
  turtle.forward(100)
  turtle.right(120)
  
turtle.exitonclick()
#062
import turtle
turtle.shape("turtle")

for i in range(0,360):
  turtle.forward(1)
  turtle.right(1)
  
turtle.exitonclick()
#063
import turtle
turtle.shape("turtle")

turtle.color("black", "green")
turtle.begin_fill()
for i in range(0, 4):
  turtle.forward(100)
  turtle.right(90)
turtle.penup()
turtle.end_fill()
turtle.forward(130)

turtle.pendown()
turtle.color("black", "yellow")
turtle.begin_fill()
for i in range(0, 4):
  turtle.forward(100)
  turtle.right(90)
turtle.penup()
turtle.end_fill()
turtle.forward(130)

turtle.pendown()
turtle.color("black", "red")
turtle.begin_fill()
for i in range(0, 4):
  turtle.forward(100)
  turtle.right(90)
turtle.penup()
turtle.end_fill()
  
turtle.exitonclick()
#064
import turtle as t
t.shape("turtle")

for i in range(0, 5):
  t.forward(100)
  t.right(144)

t.exitonclick()
#065
import turtle as t
t.shape("turtle")

t.left(90)
t.forward(100)
t.right(90)

t.penup()
t.forward(50)
t.pendown()

t.forward(100)
t.right(90)
t.forward(50)
t.right(90)
t.forward(100)
t.left(90)
t.forward(50)
t.left(90)
t.forward(100)

t.penup()
t.forward(50)
t.pendown()

t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)

t.penup()
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.pendown()

t.forward(50)

t.exitonclick()
#066
import turtle as t
t.shape("turtle")
import random
t.pensize(3)

for i in range(0, 8):
  t.color(random.choice(["red", "green", "black", "pink", "blue"]))
  t.forward(50)
  t.right(45)

t.exitonclick()
#067
import turtle as t
t.shape("turtle")
import random

for i in range(0, 10):
  for i in range(0, 8):
    t.forward(30)
    t.right(45)
  t.right(36)
  
t.exitonclick()
#068
import turtle as t
t.shape("turtle")
import random
n = random.randint(3, 10)
m = random.randint(1, 10)
l = random.randint(10, 50)
for i in range(0, m):
  for i in range(0, n):
    t.forward(l)
    t.right(360/n)
  t.right(360/m)
  
t.exitonclick()
#069

