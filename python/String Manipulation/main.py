# String manipulation and validation
# This program demonstrates string manipulation
# 2022-04-19
# jwillder

word=input("Please input a string: ")

print("Orginal word is:",word)
print("Upper case :", word.upper())
print("Lower case :", word.lower())
print("Capitalize first word :", word.capitalize())
print("Capitaize all words :", word.title())
print("There is/are", word.count("e"), "e's in this word")
print("The e character is in position", word.find("e"))
print("The string length is", len(word), "characters.")
print("Is is a digit?", word.isdigit())# numbers
print("Is it alphanumeric?", word.isalpha()) #spaces are not alpha!