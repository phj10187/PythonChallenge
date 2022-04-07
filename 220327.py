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
