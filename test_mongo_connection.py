import pymongo
from pymongo import MongoClient
import colorama 
from colorama import Fore

cluster = MongoClient("mongo_url")

db = cluster["CrowdFundingApp"]
collection = db["user"]
collection2 = db["project"]

def insert_user(fname,lname,email,password,mobile):
    user_test = {
        "firstName": fname,
        "lastName": lname,
        "Email":email,
        "Password":password,
        "Mobile":mobile
    }
    collection.insert_one(user_test)



def find_user_by_email(email):
    found_user = collection.find_one({"Email":email})
    return found_user



def find_user_by_password(password):
    f_user = collection.find_one({"Password":password})
    return f_user

def find_all_projects():
    for x in collection2.find({},{"_id":0, "user_id":0}):
        print(x)

def create_project(user_id, title, details, totalTarget,startTime,endTime ):  
    created_project = {
        "user_id": user_id,
        "Title": title,
        "Details": details,
        "Total_Target": totalTarget,
        "Start_Date": startTime,
        "End_Date":endTime
    }
    collection2.insert_one(created_project)


def update_project(user_id):
    try:
        projects_of_specific_user = list(collection2.find({"user_id":user_id}))
        print(projects_of_specific_user)

        print()
        for project in projects_of_specific_user:
            print(Fore.WHITE+project)
            
        print()    
        title_of_wanted_project = input(Fore.WHITE+"Enter the Title of the project that you want to update: ")

        for project in projects_of_specific_user:

            if project["Title"] == title_of_wanted_project:
                key = input(Fore.WHITE+"Enter the key you want to update: ")
                value = input(Fore.WHITE+"Enter the value that you want to update: ")
                collection2.find_one_and_update({"user_id":user_id, "Title": title_of_wanted_project},{"$set":{key: value}})
    except:
        print()
        print(Fore.RED + "The project you're trying to update is not found, try again") 

def delete_project(user_id):

    try:
        projects_of_specific_user = list(collection2.find({"user_id":user_id}))

        print(projects_of_specific_user)

        title_of_deleted_project = input(Fore.WHITE+"Enter the Title of the project that you want to delete: ")


        collection2.find_one_and_delete({"user_id":user_id, "Title": title_of_deleted_project})


    except TypeError:
        print(Fore.RED+"The project you are trying to delete is not found, try again")



def search_project_by_date(req_date):
    req_projects = collection2.find({"Start_Date":req_date})
    print(req_projects)


    
