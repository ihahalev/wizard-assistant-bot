from datetime import datetime
from remembrall.helpers.output_functions import colorful_wrap
@colorful_wrap
def greeting():
    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        return "Good Morning Mighty Wizard"
    elif (hour >= 12) and (hour < 16):
        return "Good afternoon Mighty Wizard"
    elif (hour >= 16) and (hour < 21):
        return ("Good Evening Mighty Wizard")
    else:
        return "Good Night Mighty Wizard"

@colorful_wrap
def farewell():
    hour = datetime.now().hour
    if hour >= 21 or hour <= 6:
        return "Good night Mighty Wizard, take care!"
    else:
        return "Have a good day Mighty Wizard!"


