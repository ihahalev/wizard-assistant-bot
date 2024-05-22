from datetime import datetime

def greeting():
    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        print(f"Good Morning ")
    elif (hour >= 12) and (hour < 16):
        print(f"Good afternoon ")
    elif (hour >= 16) and (hour < 19):
        print(f"Good Evening ")
    print(f"Welcome to the Assistant bot for wizards of the academy! Type | help | to see all bot commands") 

def farewell():
    hour = datetime.now().hour
    if hour >= 21 and hour < 6:
        print("Good night sir, take care!")
    else:
        print('Have a good day sir!')
