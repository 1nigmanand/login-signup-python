import json
import os

print("Welcome To (login / signup) ")
print("Enter (help) to see options.")
filename = input("Enter File name you want to create-:")
file = os.getcwd()+"/"+filename+".json"
if file[-1*len(filename)+5:-5] != filename:
    with open(file,"x") as dt:
        dt.write(json.dumps({}))
else: 
    with open(file,"r") as db:
        maindata = json.load(db)

    
with open(file,"r") as db:
    maindata = json.load(db)


while True:
    feature = input(">>>")
    if feature in ("1","signup"):
        while True:
            name = input("Enter Name -:")
            if name.isalpha()==True:
                while True:
                    number = input("Enter Number-:")
                    if number.isnumeric()==True:
                        while True:
                            email = input("Enter email-:")
                            if email[-10:] == "@gmail.com" and email!="@gmail.com" and email not in maindata:
                                while True:
                                    password = input("Enter password(@ and #)-:")
                                    if "@" in password and "#" in password:
                                        data_list = [name,number,password]
                                        key_list = ["Name","Number","Password"]
                                        small_dict = {}
                                        for i in range(len(data_list)):
                                            small_dict.update({key_list[i]:data_list[i]})
                                        maindata.update({email:small_dict})
                                        with open(file,"w") as data_transfer:
                                            json.dump(maindata,data_transfer,indent=7)
                                        print("Login Succssful.")
                                        break
                                    else:
                                        print("Not a strong password.")
                                break
                            else:
                                print("use (@gmail.com) in the last")
                        break
                    else:
                        print("Invalid number entered.")
                break
            else:
                print("Invalid name Entered.")
                                        
    elif feature in ("2","login"):
        gmail = input("Enter gmail-:")
        if gmail in maindata:
            passwd = input("Enter password-:")
            if maindata[gmail]["Password"] == passwd:
                print("1.update\n2.delete")
                feature = input("Enter feature:-")
                if feature in ("1" or "update"):
                    print("update choice\n1.name\n2.number\n3.password")
                    choice = input("Enter choice-:")
                    if choice in ("1","name"):
                        new_name = input("Enter new name-:")
                        maindata[email]["Name"] = new_name 
                        print("Name updated")
                    elif choice in ("2","number"):
                        new_number = input("Enter new number-:")
                        maindata[email]["Number"] = new_number
                        print("Number updated")
                    elif choice in ("3","password"):
                        old_password = input("Enter old password-:")
                        if maindata[gmail]["Password"]==old_password:
                            new_password = input("Enter new name-:")
                            maindata[email]["Password"] = new_password
                            print("password updated.")
                        else:
                            print("Incorrect password.")
                    else:
                        print("Option not available.")
    
                elif feature=="2":
                    del maindata[gmail]
                    print("Data is deleted.")
                else:
                    print("Option not available.")
    
            else:
                print("Incorrect password.")
        else:
            print("Gmail not found.")
            
            
            
    elif feature in ("3","help"):
        print("1.signup\n2.login\n3.exit")
    elif feature in ("4","exit"):
        break
    else:
        print("Command! not found.")
    with open(file,"w") as data_transfer:
        json.dump(maindata,data_transfer,indent=7)

