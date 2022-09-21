# Times Table
# This program will print out the times table (up to 12) for a given number
# 2022-04-23
# jwillder

print("\t__TIMES TABLES__")
def main():
  # Ask which times table to do
  table = input("\nWhich times table shall I do?: ")
  if not table.isdigit():
    print("ERROR: You need to enter an integer!")
    return main()
  table = int(table)
  multiplier = 1
  # Print the times table up to 12
  for product in range(table,13*table,table):
    print(multiplier, "x", table, "=", product)
    multiplier = multiplier + 1
  # Ask if they'd like another go
  again = input("\nShall I do another? (y/n) : ")
  if again == "y" or again == "Y":
    main()
  else:
    return 0
      
main()