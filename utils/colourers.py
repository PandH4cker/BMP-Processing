import sys
from colorama import Fore, Back, Style

def success(s:str):
    print(Fore.GREEN + '[+] ' + Style.RESET_ALL + s)

def error(s:str):
    print(Fore.RED + '[!] ' + Style.RESET_ALL + s, file=sys.stderr)

def info(s:str):
    print(Fore.YELLOW + '[i] ' + Style.RESET_ALL + s)