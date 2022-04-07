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
