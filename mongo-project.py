import pymongo
import os
if os.path.exists("env.py"):
    import env


MONGODB_URI = os.environ.get("MONGO_URI")
DBS_NAME = "myTestDB"
COLLECTION_NAME = "myFirstMDB"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e


def show_menu():
    print("")
    print("1. Add a record")
    print("2. Find a record by name")
    print("3. Edit a record")
    print("4. Delete a record")
    print("5. exit")

    option = input("Enter Option: ")
    return option


def get_record():
    print("")
    first = input("Enter first name > ")
    last = input("Enter last name > ")

    try:
        coll.find({"first": first.lower(), "last": last.lower()})
    except:
        print("Error accessing the database")

    if not doc:
        print("")
        print("Error! no result found.")

    return doc


def add_record():
    print("")
    first = input("Enter first name > ")
    last = input("Enter last name > ")
    dob = input("Enter dob > ")
    gender = input("Enter gender > ")
    hair_colour = input("Enter hair_colour > ")
    occupation = input("Enter occupation > ")
    nationality = input("Enter nationality > ")

    new_doc = {
        "first": first.lower(),
        "last": last.lower(),
        "dob": dob,
        "gender": gender,
        "hair_colour": hair_colour,
        "occupation": occupation,
        "nationality": nationality
    }

    try:
        coll.insert(new_doc)
        print("")
        print("Document Inserted")
    except:
        print("Error accessing the database")






def main_loop():

    while True:

        option = show_menu()
        if option == "1":
            add_record()
            print("You have selected option 1")
        elif option == "2":
            print("You have selected option 2")
        elif option == "3":
            print("You have selected option 3")
        elif option == "4":
            print("You have selected option 4")
        elif option == "5":
            conn.close()
            break
        else:
            print("Invaild option")
        print("")


conn = mongo_connect(MONGODB_URI)
coll = conn[DBS_NAME][COLLECTION_NAME]
main_loop()
