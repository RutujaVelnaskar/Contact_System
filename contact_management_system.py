import json
import re
contact={}
def add_contact():
    cid=int(input("Enter a Contact ID:"))
    cname=input("Enter a  name:")
    mobile_no=input("Enter a mobile No:")
    email_id=input("Enter a email id:")
    if not re.match(r"^[A-Za-z]+ [A-Za-z]+ [A-Za-z]+$",cname):
        print("Invalid Name")
        return   
    if not re.match(r"^[7-9][0-9]{9}$",mobile_no):
        print("Invalid Mobile Number, Give a Correted Format Mobile Number")
        return   
    if not re.match(r"^[a-z0-9]+@[a-z]+\.[a-z]{2,3}$",email_id):
        print("Invalid Email Give the Corrected Email")
        return
    try:
        with open("contact.json","r") as file:
            data=json.load(file)
    except:
        data={}
    data[str(cid)]={
        "Name":cname,
         "Mobile Number":mobile_no,
         "Email ID":email_id
    }

    with open("contact.json","w") as file:
        json.dump(data, file, indent=4)

    print("Contact Added Successfully")

def view_contact():
    
    try:
        with open("contact.json","r")as file:
            data=json.load(file)
    except:
        print("No contact found")
        return
    if not data:
        print("Not a Display Data")
        return
    for cid,details in data.items():
        print("\nContact ID:", cid)
        print("Name:", details["Name"])
        print("Mobile:", details["Mobile Number"])
        print("Email:", details["Email ID"])


def del_contact():
    cid=int(input("Enter a Contact ID:"))
    try:
        with open("contact.json", "r") as file:
            data = json.load(file)
    except:
        print("No contacts found")
        return
    if str(cid) in data:
        del data[str(cid)]

        with open("contact.json", "w") as file:
            json.dump(data, file, indent=4)
        print("Contact Delete Successfully")
    else:
        print("ID Not Found")


def update_contact():
    cid=int(input("Enter a Contact ID:"))
    try:
        with open("contact.json","r") as file:
            data=json.load(file)
    except:
        print("No Contact Found")
        return

    if str(cid) in data:
        cname=input("Enter a  name:")
        mobile_no=input("Enter a mobile No:")
        email_id=input("Enter a email id:")
        if cname:
            if not re.match(r"^[A-Za-z]+ [A-Za-z]+ [A-Za-z]+$",cname):
                print("Invalid Name")
                return
            data[str(cid)]["Name"] = cname

        if mobile_no:
            if not re.match(r"^[7-9][0-9]{9}$",mobile_no):
                print("Invalid Mobile Number, Give a Correted Format Mobile Number")
                return
            data[str(cid)]["Mobile Number"]=mobile_no

        if email_id:
            if not re.match(r"^[a-z0-9]+@[a-z]+\.[a-z]{2,3}$",email_id):
                print("Invalid Email Give the Corrected Email")
                return
            data[str(cid)]["Email ID"]=email_id
        
        with open("contact.json","w") as file:
            json.dump(data,file,indent=4)
        print("Contact Update Successfully")
    else:
        print("Contact Id Not Found")    


while True:

    print("1. Add Contact")
    print("2. View Contact")
    print("3. Delete Contact")
    print("4. Update Contact")
    print("5. Exit")

    choice=int(input("Enter Your Choice:"))

    if choice == 1:
        add_contact() 
    elif choice == 2:
        view_contact()
    elif choice == 3:
        del_contact()
    elif choice == 4:
        update_contact()
    elif choice == 5:
        print("Exit")
        break
    else:
        print("Wrong Choice Choose")
        break
