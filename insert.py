def insertInFile():
  value = input("Please enter a potential password:\n")

  if value == ':q':
    print("Bye!")
    quit()
  elif value == ':c':
    confirm = input("Reset the file ? [Y]:\n")
    if confirm == 'Y' or confirm == 'y':
      file = open("passwords.txt", "w")
      file.write("")
      file.close()
      print("Password's file cleaned")
      insertInFile()
    else:
      insertInFile()
  else:
    value = value.replace(" ", "")
    value = value.replace("'", "")
    file = open("passwords.txt", "a")
    file.write(value + "\n")
    file.close()
    insertInFile()

insertInFile()