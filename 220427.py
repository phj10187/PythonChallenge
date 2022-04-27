#069
nation_tuple = ["Korea", "USA", "france"]
for i in nation_tuple:
  print(i)
guess = input("Enter one of the countries above: ")
print(guess, "has index number", nation_tuple.index(guess))
#070
nation_tuple = ["Korea", "USA", "france"]
for i in nation_tuple:
  print(i)
number = int(input("Enter the number between 1 to 3: "))
print("Your country is", nation_tuple[number-1])
#071
sports_list = ["baseball", "basketball"]
sports_list.append(input("What's your favorite sports?: "))
sports_list.sort()
print(sports_list)
#072
