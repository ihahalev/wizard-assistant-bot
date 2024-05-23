from .constants import commands
from colorama import Fore, Style
def show_help():
    help_string = ''

    for i in commands:
        help_string += f' 💡 {Fore.CYAN}{i[0]:<16} | {i[1]:<30} | {i[2]:<12}{Style.RESET_ALL} \n'
        
    print(help_string)
