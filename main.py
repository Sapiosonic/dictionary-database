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


