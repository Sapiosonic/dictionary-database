people = {"Dave": "joiner", "Bob": "builder"}


def intro():
    print("Welcome to the Database\n")
    print("To get access, please enter your password")
    enter_password()


def enter_password():
    password = "123abc"
    entry_one = input("Enter password")
    if(len(entrey_one) < 3 and (entry_one != password)):
      print("Access Denied!")
    else:
       print("Access Granted!")
       data_base()

def data_base():
  x = int(input("1) Clear\n2) Update\n3) Print\n"))
  if x == 1:
    people.clear()
    print(people)
    print("Database Cleared")
  elif x == 2:
    updated_dictionary()
  elif x == 3:
    print(people)

def update_dictionary():
   for i in range(3):
      name = input("Enter name: ")
      job = input("Enter job: ")
      people[name] = job
      print(people)

intro()