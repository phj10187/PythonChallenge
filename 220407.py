#026
word = input("Please enter a word: ")
first = word[0].lower() #소문자 첫글자
length = len(word) 
rest = word[1:length]
if first != "a" and first != "e" and first != "i" and first != "o" and first != "u":
  newword = rest + first + "ay"
else:
  newword = word + "way"
print(newword.lower())
#027
num = float(input("Enter a number with lots of decimal places: "))
print (num * 2)
#028
num = float(input("Enter a number with lots of decimal places: "))
result = round(num * 2,2)
print (result)
#029
import math
num = int(input("Enter a number over 500: "))
answer = math.sqrt(num)
print(round(answer,2))
#030
import math
print(round(math.pi, 2))
#031
import math
radious = int(input("Enter the radious of circle: "))
area = (radious ** 2) * math.pi
print (area)
#032
import math
radious = int(input("Enter a radious of the circle: "))
depth = int(input("Enter a depth: "))
area = math.pi * (radious ** 2) * depth
print(round(area, 3))
#033
num1 = int(input("Please enter a first number over 0: "))
num2 = int(input("Please enter a second number over the first number: "))
answer = num1 // num2
remaining = num1 - (answer * num2)
print( num1, "divided by", num2,"is", answer, "with", remaining, "remaining")
#034
menuSelection = int(input("1) square\n2) triangle\n\nEnter a number: "))
if menuSelection == 1:
  length = int(input("Enter a length of one side: "))
  answer = length**2
  print("The area of your chosen shape is", answer)
elif menuSelection == 2:
  length = int(input("Enter a length of the base: "))
  height = int(input("Enter a height: "))
  answer = length * height * 0.5
  print("The area of your chosen shape is", answer)
else:
  print("The answer is wrong")
  
#035
name = input("Enter your name: ")
for i in range(0,3):
  print(name)
  
#036
  name = input("Enter your name: ")
num = int(input("how many times you want to repeat?: "))
for i in range(0,num):
  print(name)
  
#037
name = input("Enter your name: ")
for i in name:
  print(i)

#038
name = input("Enter your name: ")
num = int(input("How many times you want to repeat?: "))
for i in range(0,num):
  for i in name:
    print(i)
    
#039
num = int(input("Enter a number from 1 to 12: "))
for i in range(0,12,1):
  i = i + 1
  print(num, "x", i, "=", num * i)

  #040
  num = int(input("Enter a number below 50: "))
for i in range(50,num-1,-1):
  print (i)
  
#041
name = input("Enter your name: ")
num = int(input("Enter a number: "))
if num < 10:
  for i in range(0,num):
    print(name)
else:
  print("Too high!")
  
#042
total = 0
for i in range(0,5):
  num = int(input("Enter a number: "))
  answer = input("Do you want this number included? (y/n): ")
  if answer == "y":
    total = total + num
print(total)

#043
direction = input("Enter a count direction you want(up/down): ")
if direction == up:
  num = int(input("Enter a biggest number: "))
  for i in range(1, num)
  print(i)
elif direction = down:
  num = int(input("Enter a number beliw 20: "))
