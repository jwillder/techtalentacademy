# TTA Caesar Cipher
# This program will take a word and output cipher text using the caesar (shift) cipher
# 2022-04-20
# jwillder

print("\t\t___CAESAR CIPHER PROGRAM___\n")

# Enter a word and shift by set value of 3, output one letter at a time
print("__SHOW ASCII SHIFT VALUES__")
word = input("Enter a word: ")
for i in range(0, len(word)):
  print(i, word[i], "the ASCII value is", ord(word[i]), "shifted by 3 the value is", str(ord(word[i])+3))
print()

# Enter a word and choose the shift value, output one letter at a time
print("__SHOW SHIFTED CHARACTERS__")
word = input("Enter a word: ")
shift = int(input("Enter a shift value: "))
for i in range(0, len(word)):
  shiftedNum = ord(word[i]) + shift
  shiftedChar = chr(shiftedNum)
  print(i, word[i], "the ASCII value is", ord(word[i]), "shifted by", shift, "the character is", shiftedChar)
print()

# Enter a word, choose a shift value, output the whole shifted word
print("__CREATE CIPHERTEXT__")
word = input("Enter a word: ")
shift = int(input("Enter a shift value: "))
ciphertext = ""
for i in range(0, len(word)):
  code = ord(word[i])
  if code == 32:
    shiftcode = code
  else:
    shiftcode = code + shift
  char = chr(shiftcode)
  ciphertext = ciphertext + char
print("Your encrypted word is:",ciphertext)
print()

def main():
  print("__ENCRYPT/DECRYPT TEXT__")
  print("What would you like to do:\n")
  print("\t1. Encrypt text\n\t2. Decrypt ciphertext\n")
  choice = input("Enter choice: ")
  if choice == "1":
    encrypt()
  elif choice == "2":
    decrypt()
  else:
    print()
    main()

def encrypt():
  word = input("Enter a word: ")
  shift = int(input("Enter a shift value: "))
  ciphertext = ""
  for i in range(0, len(word)):
    # get the ascii code number
    code = ord(word[i])
    # if space don't shift
    if code == 32:
      shiftcode = code
    # add shift to uppercase letter
    elif code in range(65,91):
      shiftcode = uppershift(code, shift)
    # add shift to lowercase letter  
    elif code in range(97,123):
      shiftcode = lowershift(code, shift)
    # invalid non-alpha character so ask for new word
    else:
      print("The word contains a non-alpha character, enter another.")
      encrypt()
    # convert shifted code to letter
    char = chr(shiftcode)
    ciphertext = ciphertext + char
  print("Your encrypted word is:",ciphertext)
  choice = input("\nEncrypt or decrypt another word?(y/n): ")
  if choice == "y" or choice == "Y":
    print()
    main()
  else:
    return

def uppershift(code, shift):
  shiftcode = code + shift
  while shiftcode > 90:
    shiftcode = shiftcode - 26
  return shiftcode

def lowershift(code, shift):
  shiftcode = code + shift
  while shiftcode > 122:
    shiftcode = shiftcode - 26
  return shiftcode

def decrypt():
  word = input("Enter a word: ")
  shift = int(input("Enter a shift value: "))
  ciphertext = ""
  for i in range(0, len(word)):
    code = ord(word[i])
    if code == 32:
      shiftcode = code
    else:
      shiftcode = code - shift
    char = chr(shiftcode)
    ciphertext = ciphertext + char
  print("Your decrypted word is:",ciphertext)
  choice = input("\nEncrypt or decrypt another word? (y/n): ")
  if choice == "y" or choice == "Y":
    print()
    main()
  else:
    return

main()