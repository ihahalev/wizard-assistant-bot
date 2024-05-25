from colorama import Fore, Style

def change_text_color(text, color=Fore.GREEN):
    # return f"{color}{text}{Style.RESET_ALL}"
    print(color + text + Style.RESET_ALL)



def colorful_wrap(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print (f"{Fore.GREEN}{result}{Style.RESET_ALL}")
    return wrapper


