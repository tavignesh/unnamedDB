# for now i am not getting any idea how to get input to edit the database
# you can clone and test this also create an issue in git if any bug is found
# just edit a file for yourself in name of "db<yourusername>.json" inside folder clusterdata and test other feratures pls

import json
import pickle
import csv
import os


def login():

    while True:

        crt = input("To Login 1\nTo create an account type 2\n")

        try:
            crt = int(crt)
        except:
            print("")

        if (str(type(crt)) != "<class 'int'>") or int(crt) not in [1,2]:
            print("Enter a valid option or get lost\n")
        else:
            Uname = input("Enter Username:")

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
    ender = 0
    while ender == 0:
        print("Enter an option below\n1. View your collection\n2. Edit your collection(or create a new one)\n3. Delete your whole collection\n4. Logout")
        chois = input()

        try:
            chois = int(chois)
        except:
            pass
        while str(type(chois)) != "<class 'int'>" or chois not in [1,2,3,4,5]:
            print("Enter a valid choice!!")
            chois = input()
            try:
                chois = int(chois)
            except:
                pass
            if chois == 5:
                ender = 1
                return False

        if chois == 1:
            if os.path.exists(f"clusterdata\\db{Uname}.json"):
                print("Your collection is available")
                try:
                    userfile = open(f"clusterdata\\db{Uname}.json", "r")
                    usercoll = json.load(userfile)
                    userfile.close()
                except Exception as e:
                    if str(e) != "EOFError":
                        try:
                            userfile.close()
                        except:
                            pass
                        print("an error occored while opening your collection :", e)
                    else:
                        try:
                            userfile.close()
                        except:
                            pass
                        print(usercoll)
                        if usercoll == {}:
                            print("your collection is empty!")
                        else:
                            print("Your Collection is displayed below\n", usercoll)
            else:
                print("You don't have a collection\n")

        elif chois == 2:
            if os.path.exists(f"clusterdata\\db{Uname}.json"):
                print("Select an entry from below and type it here as it is to access its sub entries:\n")
            else:
                print("you don't have a collection want to create a new one? (1 or 0)")
                reat = input()
                try:
                    reat = int(reat)
                except:
                    pass
                while str(type(reat)) != "<class 'int'>" or reat not in [1,0]:
                    print("enter a valid option (1 or 0)")
                    reat = input()
                    try:
                        reat = int(reat)
                    except:
                        pass
                if reat == 0:
                    pass
                elif reat == 1:
                    try:
                        userfile = open(f"clusterdata\\db{Uname}.json", "w")
                        emtdic = {}
                        json.dump(emtdic, userfile)
                        userfile.flush()
                        userfile.close()
                        print("Created!\n")
                    except Exception as e:
                        print("An error occured while creating:", e)
                        try:
                            userfile.close()
                        except:
                            pass


        elif chois == 3:
            if os.path.exists(f"clusterdata\\db{Uname}.json"):
                print("Your collection is available")
                try:
                    userfile = open(f"db{Uname}.json", "rb")
                    usercoll = json.load(userfile)
                except Exception as e:
                    if str(e) != "EOFError":
                        try:
                            userfile.close()
                        except:
                            pass
                        print("an error occored while opening your collection :", e)
                    else:
                        try:
                            userfile.close()
                        except:
                            pass
                        print(usercoll)
                        if usercoll == {}:
                            print("your collection is empty, what do you want to delete?")
                        else:
                            try:
                                deluserfile = open(f"clusterdata\\db{Uname}.json", "wb")
                                json.dump({}, deluserfile)
                                deluserfile.close()
                                print("Collection successfully deleted!")
                            except Exception as e:
                                print("an error occured while deleting :", e)
                                try:
                                    deluserfile.close()
                                except:
                                    pass
            else:
                print("You don't have a collection what do you want to delete!!!\n")

        elif chois == 4:
            print("You are logged out!\n")
            return False

        else:
            print("invalid choiceee\n")


                            








try:
    fdfdfd = main()
    while fdfdfd == False:
        fdfdfd = main()
    print("end of code!!")
except Exception as ea:
    print("Error Occured:", ea)
