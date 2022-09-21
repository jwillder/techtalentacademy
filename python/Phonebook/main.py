# TTA Phone Book
# Create a phone book with interactions menu to demonstrate use of SQLite
# 2022-04-27
# jwillder

import sqlite3
import time

# Connect to SQLite database
with sqlite3.connect("PhoneBook.db") as db:
  cursor=db.cursor()

# Create phone book table if it doesn't exist
cursor.execute("CREATE TABLE IF NOT EXISTS phonebook \
  (id integer PRIMARY KEY, \
  firstName text NOT NULL, \
  surName text NOT NULL, \
  homeNumber integer NOT NULL, \
  mobileNumber integer NOT NULL);")

def main():
  print("\n\t___PHONE BOOK___")
  option = input("""
What would you like to do?
  1. View the phone book
  2. Add to the phone book
  3. Search for a surname
  4. Delete person from the phone book
  5. See just the home number for a person
  6. View the phone book sorted by surname
  9. Quit
>>> """)
  
  if option.isdigit() == False:
    print ("Please enter a valid number")
    main()
  if option == "1":
    viewAll()
  elif option == "2":
    addPerson()
  elif option == "3":
    searchSurname()
  elif option == "4":
    deletePerson()
  elif option == "5":
    viewHomeNumber()
  elif option == "6":
    sortSurname()
  elif option == "9":
    return 0
  else:
    print("Unrecognised option, try again.")
    main()
    
# Neatly displays database records in columns
def printTable(records):
  # Set minimum column widths
  idWidth = 3
  fnWidth = 12
  snWidth = 12
  hnWidth = 12
  mnWidth = 12
  # Increase column width if any records are longer than min width above
  for record in records:
    if len(str(record[0])) > idWidth:
      idWidth = record[0]
    if len(record[1]) > fnWidth:
      fnWidth = len(record[1])
    if len(record[2]) > snWidth:
      snWidth = len(record[2])
    if len(str(record[3])) > hnWidth:
      hnWidth = len(str(record[3]))
    if len(str(record[4])) > mnWidth:
      mnWidth = len(str(record[4]))

  # Display column labels using widths set above
  print("ID".ljust(idWidth), \
    "First Name".ljust(fnWidth), \
    "Surname".ljust(snWidth), \
    "Home Number".ljust(hnWidth), \
    "Mobile Number".ljust(mnWidth))
  
  # Display records using widths set above
  for record in records:
    print(str(record[0]).ljust(idWidth),\
      record[1].ljust(fnWidth),\
      record[2].ljust(snWidth),\
      str(record[3]).ljust(hnWidth),\
      str(record[4]).ljust(mnWidth))

# View all records
def viewAll():
  print("\n\t__View Phone Book__\n")
  # Check there are records to display
  cursor.execute("SELECT COUNT(id) FROM phonebook")
  if cursor.fetchone()[0] == 0:
    print("There are no entries to display.")
    main()
  # Get all records and call printTable function to display them
  cursor.execute("SELECT * FROM phonebook")
  printTable(cursor.fetchall())
  time.sleep(1)  
  main()

# Add a new person to the phone book
def addPerson():
  print("\n\t__Add Person To Phone Book__\n")
  newID = input("Unique ID: ")
  firstName = input("First name: ")
  surName = input("Surname: ")
  homeNumber = input("Home number: ")
  mobileNumber = input("Mobile number: ")
  # Add person to the database and save
  cursor.execute("INSERT INTO phonebook \
    (id, firstName, surName, homeNumber, mobileNumber) \
    VALUES (?, ?, ?, ?, ?)", \
    [newID, firstName, surName, homeNumber, mobileNumber])
  db.commit()
  main()

# Search by surname
def searchSurname():
  print("\n\t__Search For A Surname__\n")
  surName = input("Enter a surname: ")
  # Get matching records and call printTable function to display them
  cursor.execute("SELECT * FROM phonebook WHERE surName=?",[surName])
  printTable(cursor.fetchall())
  time.sleep(1)
  main()

# Delete person from the phone book
def deletePerson():
  print("\n\t__Delete A Person__\n")
  id = int(input("Enter ID to delete: "))
  # Delete person by id from database and save, then show phone book to prove deletion
  cursor.execute("DELETE FROM phonebook WHERE id=?",[id])
  db.commit()
  viewAll()
  main()

# View home number for a particular ID
def viewHomeNumber():
  print("\n\t__View Home Number__\n")
  id = int(input("Enter ID for home number: "))
  # Get selected data from database
  cursor.execute("SELECT firstName, surName, homeNumber \
    FROM phonebook WHERE id=?",[id])
  result = cursor.fetchone()
  print("Home number for", result[0], result[1], "is:", result[2])
  time.sleep(1)
  main()

# View phone book sorted by surname
def sortSurname():
  print("\n\t__View Phone Book Sorted By Surname__\n")
  # Check there are records to display
  cursor.execute("SELECT COUNT(id) FROM phonebook")
  if cursor.fetchone()[0] == 0:
    print("There are no entries to display.")
    main()
  # Get all entries sorted by ascending surname
  cursor.execute("SELECT * FROM phonebook ORDER BY surname ASC")
  printTable(cursor.fetchall())
  time.sleep(1)
  main()

main()