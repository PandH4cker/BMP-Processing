import sys
from colorama import Fore, Back, Style

def success(s:str):
    print(toGreen('[+] ') + s)

def error(s:str):
    print(toRed('[!] ') + s, file=sys.stderr)

def info(s:str):
    print(toYellow('[i] ') + s)

def toRed(s:str):
    return Fore.RED + s + Style.RESET_ALL

def toGreen(s:str):
    return Fore.GREEN + s + Style.RESET_ALL

def toYellow(s:str):
    return Fore.YELLOW + s + Style.RESET_ALL

def toBlue(s:str):
    return Fore.BLUE + s + Style.RESET_ALL

def toMagenta(s:str):
    return Fore.MAGENTA + s + Style.RESET_ALL 

def toCyan(s:str):
    return Fore.CYAN + s + Style.RESET_ALL