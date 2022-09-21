# Conversion And Caesar Cipher Program
# This program converts integers to a choice of binary, hex, and ascii. It can also encrypt and decrypt text with the Caesar cipher.
# 2022-04-25
# jwillder

def main():
  # Intro text and choices
  print("""\t___INTEGER CONVERSION AND CAESAR CIPHER PROGRAM___\n
What would you like to convert?
    1. Binary
    2. Hex
    3. ASCII
    4. Caesar Cipher
    9. Quit program""")
  choice = input(">>> ")

  # Process selection
  if choice == "1":
    convertBinary()
  elif choice == "2":
    convertHex()
  elif choice == "3":
    convertAscii()
  elif choice == "4":
    caesarCipher()
  elif choice == "9":
    return 0
  else:
    print("\nInvalid selection\n")
    return main()

  # Ask to convert another number
  again = input("\nWould you like to convert another? (y/n): ")
  if again == "y" or again == "Y":
    print()
    return main()
  else:
    return  

def convertBinary():
  print("\n\t__Binary Conversion__\n")
  number = input("Enter a number to convert to binary: ")
  if not number.isdigit():
    print("You need to enter a number.")
    return convertBinary()
  number = int(number)
  print(number, "in binary format is:", bin(number).lstrip("0b"))

def convertHex():
  print("\n\t__Hex Conversion__\n")
  number = input("Enter a number to convert to hex: ")
  if not number.isdigit():
    print("You need to enter a number.")
    return convertHex()
  number = int(number)
  print(number, "in hex format is:", hex(number).lstrip("0x"))

def convertAscii():
  print("\n\t__ASCII Conversion__\n")
  number = input("Enter a number to convert to ASCII: ")
  if not number.isdigit():
    print("You need to enter a number.")
    return convertAscii()
  number = int(number)
  print(number, "in ASCII character is:", chr(number))

def caesarCipher():
  print("\n\t__Caesar Cipher__\n")
  print("""Would you like to encrypt or decrypt?
  1. Encrypt
  2. Decrypt""")
  choice = input(">>> ")
  if choice == "1":
    caesarEncrypt()
  elif choice == "2":
    caesarDecrypt()
  else:
    print("Invalid choice, please enter again")
    return caesarCipher()

def caesarEncrypt():
  print("\n\t__Caesar Cipher Encryption__\n")

  # Get text to encrypt
  text = input("Enter text to encrypt: ")
  # Check the text is not empty
  if text == "":
    print("You need to enter some text.")
    return caesarEncrypt()

  # Get shift value
  shift = input("Enter a shift value: ")
  # Check shift value is an integer
  if not shift.isdigit():
    print("You need to enter a number for the shift value.")
    return caesarEncrypt()
  shift = int(shift)

  # Iterate over the characters in the text and encrypt
  ciphertext = ""
  for i in range(0, len(text)):
    # Get the ascii code number
    code = ord(text[i])
    # If space don't shift
    if code == 32:
      shiftcode = code
    # Add shift to uppercase letter
    elif code in range(65,91):
      shiftcode = code + shift
      while shiftcode > 90:
        shiftcode = shiftcode - 26
    # Add shift to lowercase letter  
    elif code in range(97,123):
      shiftcode = code + shift
      while shiftcode > 122:
        shiftcode = shiftcode - 26
    # Invalid non-alpha character so ask for new text
    else:
      print("The text contains a non-alpha character, only use letters.")
      return caesarEncrypt()
    # Convert shifted code to letter
    char = chr(shiftcode)
    ciphertext = ciphertext + char

  # Display the encrypted text
  print("Your encrypted text is:",ciphertext)

def caesarDecrypt():
  print("\n\t__Caesar Cipher Decryption__\n")

  # Get text to decrypt
  text = input("Enter text to decrypt: ")
  # Check the text is not empty
  if text == "":
    print("You need to enter some text.")
    return caesarDecrypt()

  # Get shift value
  shift = input("Enter a shift value: ")
  # Check shift value is an integer
  if not shift.isdigit():
    print("You need to enter a number for the shift value.")
    return caesarDecrypt()
  shift = int(shift)

  # Iterate over the characters in the text and decrypt
  ciphertext = ""
  for i in range(0, len(text)):
    # Get the ascii code number
    code = ord(text[i])
    # If space don't shift
    if code == 32:
      shiftcode = code
    # Add shift to uppercase letter
    elif code in range(65,91):
      shiftcode = code - shift
      while shiftcode < 65:
        shiftcode = shiftcode + 26
    # Add shift to lowercase letter  
    elif code in range(97,123):
      shiftcode = code - shift
      while shiftcode < 97:
        shiftcode = shiftcode + 26
    # Invalid non-alpha character so ask for new text
    else:
      print("The text contains a non-alpha character, only use letters.")
    # Convert shifted code to letter
    char = chr(shiftcode)
    ciphertext = ciphertext + char

  # Display the decrypted text
  print("Your decrypted text is:",ciphertext)

main()