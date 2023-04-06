import re
import colorama 
from colorama import Fore
import datetime

def main_menu():
    print()
    print(Fore.BLACK+"---------------------------------------------")
    print(Fore.WHITE+"| Please, Select an option from 1-3:        |")
    print(Fore.BLACK+"---------------------------------------------")
    print(Fore.WHITE+"| 1- Register                               |")
    print(Fore.BLACK+"--------------------------------------------")
    print(Fore.WHITE+"| 2- Login                                  |")
    print(Fore.BLACK+"--------------------------------------------")
    print(Fore.WHITE+"| 3- Exit                                   |")
    print(Fore.BLACK+"---------------------------------------------\n")

def validate_password(password):  
    if len(password) < 8 or not re.search("[a-z]", password) or not re.search("[A-Z]", password) or not re.search("[0-9]", password):  
        return False  
    else:
        return True  

def validate_date(date_time):
    date_format = '%Y/%m/%d'
    try:
        dateObject = datetime.datetime.strptime(date_time, date_format)
        return True
    except ValueError:
        return False


def project_menu():
    print()
    print(Fore.BLACK+"---------------------------------------------")
    print(Fore.WHITE+"| Please, Select an option from 1-6:        |")
    print(Fore.BLACK+"---------------------------------------------")
    print(Fore.WHITE+"| 1- Create Project                         |")
    print(Fore.BLACK+"--------------------------------------------")
    print(Fore.WHITE+"| 2- View Projects                          |")
    print(Fore.BLACK+"--------------------------------------------")
    print(Fore.WHITE+"| 3- Edit Project                           |")
    print(Fore.BLACK+"---------------------------------------------")
    print(Fore.WHITE+"| 4- Delete Project                          |")
    print(Fore.BLACK+"---------------------------------------------")
    print(Fore.WHITE+"| 5- Search for Projects by Date             |")
    print(Fore.BLACK+"---------------------------------------------")
    print(Fore.WHITE+"| 6- Exit                                   |")
    print(Fore.BLACK+"---------------------------------------------\n")