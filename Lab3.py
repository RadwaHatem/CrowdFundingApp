import re
import colorama 
from colorama import Fore
from test_mongo_connection import delete_project,update_project,create_project,find_all_projects,insert_user, find_user_by_email, find_user_by_password
from functions import main_menu, validate_password, project_menu, validate_date
print()
print(Fore.GREEN+"                 Welcome to the Crowd-Funding Console App  \n")


main_menu()
choice = input(Fore.WHITE+"\nYour number will be: ")

while True:

    if choice == '1':
        print()
        print(Fore.BLACK+"***************************************************************")
        print(Fore.GREEN+"|              Welcome to the Registeration Page              |")
        print(Fore.BLACK+"***************************************************************\n")

        print()

        while True:
            fname = input(Fore.WHITE+"Enter your firstName: ")
            if fname == '' or fname.isalpha() == False:
                print(Fore.RED+"Please enter a valid firstName ")
        
            else:
                break

        print()

        while True:
            lname = input(Fore.WHITE+"Enter your lastName: ")
        
            if lname == '' or lname.isalpha() == False: 
                print(Fore.RED + "Please enter a valid lastName ")
            else:
                break
        print()

        while True:
            try:
                email = input(Fore.WHITE+"Enter your Email: ")
                regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
                foundUser = find_user_by_email(email)
                if re.search(regex, email):
                    if foundUser["Email"] == email:
                        print(Fore.RED+"This Email is taken, try again: ")
                    else:
                        break
                else:
                        print(Fore.RED+"Please enter a valid Email: ")

            except:
                break
                      
        print()
        while True:
            mobile = input(Fore.WHITE+"Enter your Mobile Number: ")
            reg = "^(\+201|01|00201)[0-2,5]{1}[0-9]{8}"
            if re.search(reg,mobile):
                break
            else:
                print(Fore.RED+"Please enter a valid Egyptian mobile number ")

        print()
        while True:
            password = input(Fore.WHITE+"Enter your password: ")
            pass_validation = validate_password(password)
            if pass_validation == True:
                break
            else:
                print(Fore.RED+"Please enter a valid password of at least 8 characters")

        insert_user(fname,lname,email,password,mobile)

        print()
        while True:
            confirm_password = input(Fore.WHITE+"Confirm your password: ")
            if confirm_password == password:
                 break
            else:
                print(Fore.RED+"Your passwords don't match, try again")

        print()
        print(Fore.BLUE+"User has Registered Successfully \n")
        main_menu()

        choice = input(Fore.WHITE+"\nYour number will be: ")

    # """-----------------------------------------------------------------"""
    
    elif choice == "2":

        found_user = {}
        print()
        print(Fore.BLACK+"***************************************************************")
        print(Fore.GREEN+"|              Welcome to the Login Page                      |")
        print(Fore.BLACK+"***************************************************************\n")

        print()
       
        while True:       
            useremail = input(Fore.WHITE+"Enter your Email: ")
            found_user = find_user_by_email(useremail)
            try:
                if found_user["Email"] == useremail:
                    break
                else:
                    print(Fore.RED+"your email doesn't exist, try again")
            except TypeError:
                print(Fore.RED+"your email doesn't exist, try again")

        print()
        while True:
            userpass = input(Fore.WHITE+"Enter your Password: ")

            f_user = find_user_by_password(userpass)
            try:
                if f_user["Password"] == userpass:
                    break
                else:
                    print(Fore.RED+"wrong password, try again")
            except TypeError:
                print(Fore.RED+"wrong password, try again")

        
        print(Fore.BLUE+"User has logged in Successfully \n")

        while True:
            print()

            project_menu()
            ch = input(Fore.WHITE+"\nYour number will be: ")

            if ch == "1":

                print()
                while True:
                    title = input(Fore.WHITE+"Enter the Title of your project: ")
                    if title == '': 
                        print(Fore.RED + "Please enter a valid Title: ")
                    else:
                        break

                print()
                while True:
                    details = input(Fore.WHITE+"Enter the Details of your project: ")
                    if details == '':
                        print(Fore.RED + "Please enter a valid Details: ")
                    else:
                        break

                print()
                while True:
                    totalTarget = input(Fore.WHITE+"Enter your Target: ")
                    if totalTarget == '' or totalTarget.isalpha == True:
                         print(Fore.RED + "Please enter a valid Target: ")
                    else:
                        break

                print()
                while True:
                    startTime = input(Fore.WHITE+"Enter the Start Date of your project: ")
                    validated_start_time = validate_date(startTime)
                    if validated_start_time == True:
                         break
                    else:
                        print(Fore.RED + "Please enter a valid Date in the %Y/%m/%d format: ")

                print()
                while True:
                    endTime = input(Fore.WHITE+"Enter the End Date of your project: ")
                    validated_end_time = validate_date(endTime)
                    if validated_end_time == True:
                         break
                    else:
                         print(Fore.RED + "Please enter a valid Date in the %Y/%m/%d format: ")

                user_id = found_user["_id"]

                create_project(user_id,title,details,totalTarget,startTime,endTime)

            
            elif ch == "2":

                find_all_projects()
                
                

            elif ch == "3":

                update_project(found_user["_id"])
                
            elif ch == "4":

                delete_project(found_user["_id"])
        


                # """******************************"""

        main_menu()
        choice = input(Fore.WHITE+"\nYour number will be: ")

    # """---------------------------------------------------"""

    elif choice == "3":
        break






        
    



       
    
        
        

