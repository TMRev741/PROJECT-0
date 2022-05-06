import pymongo
from pymongo import MongoClient
import matplotlib.pyplot as plt
import numpy as np
from numpy import random
from datetime import datetime
from pprint import pprint
#Connects to Mongo
cluster = MongoClient("mongodb://localhost:27017/")
#Tells which database to use
db = cluster["students"]
#Tells which table Collection to use

#Use table name or collection name. Not database name
#db.Records.create_index([("Actors" , -1)])
print("Loading Database...")
print("Student database system online")
print("Connecting...")
print("Connected!")
def menu():
    print("[View Students]")
    print("[Add/Delete Student]")
    print("[Update Grades]")
    print("[exit]")
    s_info = db["s_info"]
# OP GOES INTO IF AND ELSE STATEMENTS RIGHT UNDER


    op = input("Enter your option to View/Add/Delete/Update/Exit:  ")
# This area will display the menu options then the actions of each

    if op == ("View"):
        print("Selected: Viewing Students Information")
        #THIS FUNCTION WILL DISPLAY STUDENT INFORMATION WITHOUT OBJECT ID, GRADE, AND STUDENT ID
        cursor = s_info.find({}, {"_id":0, "Grade":0, "s_id":0})
        for document in cursor:
            print(document)

        #WHEN YOU TYPE THE STUDENT NAME, THE FULL INFORMATION OF STUDENT (including excluded)
        Students = (input("Please Insert Student's FIRST Name: "))
        query = {"First_Name": Students}
        l = s_info.find(query, {"_id": 0})
        for d in l:
            print("Viewing", d)
        menu()

#THIS WILL ADD THE FULL STUDENT NAME ALONG WITH A RANDOMIZED ID NUMBER
    elif op == "Add":
        print("Selected: Adding Student")
        if op == "Add":
            loop = True
            while loop:
                Students_N = input("Please Insert New Student (Full Name): ")
                try:
            #Splits using [1] and [0]. Will print out 2 things in the quotation marks if spaced. 0 is first then 1 and so forth
                    first = Students_N.split(" ")
                    last = first[1]

                    loop = False
                except:
                    loop = True
                    print("You forgot the last name, dummy.")
            Grad = str("Empty")
            #WILL RANDOMIZE ID NUMER
            id = random.randint(99999999)
            #WILL INSERT NAME AND ID NUMBER INTO THE "s_info" COLLECTION
            insert = {"First_Name": first[0], "Last_Name": last,"Grade": Grad, "s_id": id}
            s_info.insert_one(insert)

            cursor = s_info.find({}, {"_id": 0, "Grade": 0})
            for document in cursor:
                print(document)
            print("New ID successfully created for", first, ": ID", id, " [No Grade within Slot]")
            menu()


            #{} Informs of mongo DB
            #WILL INSERT INTO DATABASE
#WILL DELETE WHATEVER ID INTEGER YOU ENTER THAT'S WITHIN THE DATABASE
    elif op == "Delete":
            print("Selected: Delete Student Grade")
            cursor = s_info.find({}, {"_id": 0, "Grade": 0}).sort("First_Name")
            for document in cursor:
                print(document)
            ID = int(input("Please Insert Student ID to Delete: "))
            #WILL LOOK FOR STUDENT ID WITHIN s_id COLUMN TO DELETE
            query = {"s_id": int(ID)}
            s_info.delete_one(query)

            cursor = s_info.find({}, {"_id": 0, "Grade": 0, "s_id": 0}).sort("First_Name")
            for document in cursor:
                print(document)
            print("deleted",  ID, "from database")
            menu()


#WILL UPDATE THE DATABASE GRADES AND/OR NAMES
    elif op == "Update":
                        cursor = s_info.find({}, {"_id": 0, "Grade": 0}).sort("First_Name")
                        for document in cursor:
                            print(document)
                        ID = int(input("Please insert ID: "))
                        Students_N = input("Please Insert Grade: ")
                            # Splits using [1] and [0]. Will print out 2 things in the quotation marks if spaced. 0 is first then 1 and so forth
                            # WILL UPDATE THE GRADE OF ANY ID SET IN THE INPUT
                        print("Please Insert Grade: ")
                        print("Grade updated to ", Students_N)
                        query = {"s_id": ID}
                        B = {"$set": {"Grade": Students_N}}
                        s_info.update_one(query, B)

                        cursor = s_info.find({}, {"_id": 0}).sort("First_Name")
                        for document in cursor:
                            print(document)

                        menu()



    elif op == "Exit":
        print("Have a nice day")
        quit()
    else:
        print("NOTE: Type: 'View', 'Add', 'Delete', 'Exit'")
        menu()
#FUNCTIONS OF LOGIN
def auth():
    name = input("Enter Username: ")
    if name == "Trathen":
        pw = input("Enter Password: ")
        if pw == "Trathen24":
            print("Welcome " + name + "!" )
            #THIS WILL SHOW THE TIME YOU HAVE LOGGED IN
            now = datetime.now()
            dt_string = now.strftime("%m/%d/%Y %I:%M:%S %p ")
            print("Login Time:", dt_string)
#ENTER "menu()" TO HAVE IT TO GO BACK TO THE MENU STATEMENT
            menu()

# INCORRECT USERNAME CODING
        else:
        # Tab when you open a new loop (Or a loop within a loop)
            loop = True
            while loop:
                pwi = input("Incorrect password. Try again? y/n ")
                if pwi == "y".lower():
                    auth()
                if pwi == "n".lower():
                    print("Exiting... Have a nice day")
                    quit()
# INCORRECT USERNAME CODING
    else:
        if name != "Trathen".lower():
            uni = ""
            while uni != "n":
                uni = input("incorrect username. Try again? y/n ")
                if uni == "y".lower():
                    auth()


            else:
                print("Exiting... Have a nice day")
                quit()
def main():
    auth()
if __name__ == "__main__":
    main()

#If you get the correct name and password
#Creating a new user
#We want the update feature (Change or update ability of grade)
#We want a search feature that will display users by grades or ids
#We want a delete function (Remove user or grade)

#Search all who have a certain grade

