#052
import random
num = random.randint(0, 100)
print(num)
#053
import random
fruit = random.choice(["apple", "banana", "cherry"])
print(fruit)
#054
import random
face = random.choice(["h", "t"])
choice = input("which one you want to choose?(h/t): ")
if choice == face:
  print("You win!")
else:
  print("Bad luck")
print("The answer is",face)
#055
import random
num = random.randint(1, 5)
answer = int(input("Enter a number between 1 to 5: "))
if answer == num:
  print("Well done")
else:
  if answer > num: 
    print("Too high")
  else:
    print("Too low")
  answer = int(input("Enter a number: "))
  if answer == num:
    print("Corect")
  else:
    print("You lose")
#056
import random
num = random.randint(1, 10)
correct = False
while correct == False:
  guess = int(input("Enter a number: "))
  if guess == num:
    correct = True
#057
import random
num = random.randint(1, 5)
correct = False
while correct == False:
  guess = int(input("Enter a number: "))
  if guess == num:
    correct = True
  elif guess > num: 
    print("Too high")
  else:
    print("Too low")
#058
import random
times = 5
score = 0
for i in range (0, 5):
  num1 = random.randint(0,10)
  num2 = random.randint(0,10)
  answer = num1 + num2
  print(num1, "+", num2,"=")
  guess = int(input("Enter your answer: "))
  if guess == answer:
    score = score + 1
print("Your score is", score, "out of 5")
#059
import random
colour = random.choice(["BLUE", "GREEN"])
print("BLUE, GREEN")
choice = input("which one you want to choose?: ")
choice.upper()
if choice == colour:
  print("Well done")
else:
  if colour == "BLUE":
     print("You are probably feeling BLUE right now")
  elif colour == "GREEN":
    print("I bet you are GREEN with envy")
    print(colour)

#---------------------------HEART-------------------
import turtle
turtle.shape("turtle")
turtle.right(270)
for i in range(0, 36):
  turtle.forward(3)
  turtle.right(5)
  
turtle.right(180)

for i in range(0, 36):
  turtle.forward(3)
  turtle.right(5)
  
for i in range(0, 3):
  turtle.forward(10)
  turtle.right(15) 
  
turtle.forward(60)
for i in range(0, 3):
  turtle.left(7)
  turtle.forward(7)
turtle.right(125)
for i in range(0, 3):
  turtle.left(7) 
  turtle.forward(7)
turtle.forward(60)

for i in range(0, 3):
  turtle.right(15) 
  turtle.forward(10)

turtle.exitonclick()

#060
    



    
