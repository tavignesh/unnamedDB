import json
import pickle
import csv
import os
# os.path.exists("file.txt")


def login():

    while True:

        crt = input("[+] To Login : 1 \n[+] To create an account type : 2\n")

        try:
            crt = int(crt)
        except:
            print("")

        if (str(type(crt)) != "<class 'int'>") or int(crt) not in [1,2]:
            print("Enter a valid option or get lost\n")
        else:
            Uname = input("Enter Username: ")

            try:
                dataids = open("dataid.dat", "rb")
                og = pickle.load(dataids)
            except Exception as e:
                dataids.close()

            if Uname in og:
                if int(crt) == 1:
                    print("Welcome, Enter your pass or 0 to exit\n")
                    pasw = input()
                    if str(og[Uname]) == pasw:
                        print("Successfully logged in!")
                        return Uname
                    elif str(pasw) == "0":
                        print("exiting!!\n")
                    else:
                        print("Wrong password please relogin\n")
                elif int(crt) == 2:
                    print("Sorry! Someone has already taken that Username choose something else!\n")
            elif Uname not in og:
                if int(crt) == 1:
                    print("The Username you entered does not exist\n")
                elif int(crt) == 2:
                    print("Enter a new password\n")
                    pasw = input()
                    pasw2 = input("Reenter password\n")
                    while (len(list(pasw)) <= 7) or pasw != pasw2:
                        print("Enter a password greater than 7 letters also enter it same both times!\n")
                        pasw = input()
                        pasw2 = input("Reenter the password\n")
                    og[Uname] = pasw
                    try:
                        dataids = open("dataid.dat", "wb")
                        pickle.dump(og, dataids)
                        dataids.close()
                    except Exception as e:
                        print("an error occured: ", e)
                        dataids.close()
                    print("New user has created an account and logged in successfully")
                    return Uname

def main():
    Uname = login()
    print(f"Welcome to our database! you have successfully logged in with Username: {Uname}")
    print("well thats all for now :)")

try:
    main()
except Exception as ea:
    print("eError Occured:", ea)



