from system.model.staff import Client
from system.model.manager_cashier import Manager
from system.model.login import Login
from system.model.pdf_ticket import *
from datetime import datetime
import sys
import time

login_security = Login()
manager_cashier = Manager()
client = Client()
dates = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def continues():
    input("Try any key to be continue....." + "\n" + "\n")

def cashiers():
    user = 1
    while True:
        print("===========================================")
        print("welcome to system cinema control cashier")
        print("===========================================")
        print("[ 1 ] View movie")
        print("[ 2 ] Add Cart to pay")
        print("[ 3 ] Remove the movie")
        print("[ 4 ] logout")
        print("[ 5 ] request something to the admin")
        choice = input("select the option:")

        if choice == '1':
            manager_cashier.view_data()
            continues()

        elif choice == '2':
            while True:
                space = []
                manager_cashier.view_data()
                how_many, choose = manager_cashier.payment()
                g = manager_cashier.check_outs1()
                if g == 0:
                    continues()
                    break
                for i in range(how_many):
                    while True:
                        try:
                            seat = int(input("Enter seat number from 1-100: "))
                            if seat <= 100:
                                data = client.saving()
                                already_book = any(
                                    e['seat'] == seat and e['hall'] == choose
                                    for e in data
                                )
                                if already_book:
                                    print("‼️ This seat has been book by someone in this hall")

                                else:
                                    client.enter_data(seat=seat, halls=choose, user=user)
                                    space.append(seat)
                                    print(f"✅ Your seat booking [hall {choose} - seat {seat}] is confirm")
                                    break

                            elif seat > 100:
                                print("our hall dont have 100 up seat sorry")
                        except ValueError:
                            print("It's not a number!!")
                user += 1
                print(f"Your seats : {space} , in hall  {choose} Thank you! ")
                for i in range(10):
                    sys.stdout.write("\rwaiting 5 second to create PDF" + "." * (i % 6))
                    sys.stdout.flush()
                    time.sleep(0.5)
                print("\nDone!!")
                mainss()
                continues()
                break

        elif choice == '3':
            manager_cashier.view_data()
            try:
                deletes = int(input("enter [HALL] to remove:"))
                manager_cashier.removing(delete=deletes)
                continues()
            except ValueError:
                print("please enter valid ID")
                continues()

        elif choice == '4':
            break

        elif choice == '5':
            text = input("say something you want to request admin:")
            with open("request_from_cashier/request_report.txt", "a",newline="") as f:
                 f.write(f"from cashier ==>{dates+ "  " + text  +  "\n" + "\n"}")
            print("Thank you for requesting i will check later !! ")
            continues()

def managers():
    user = 1
    while True:
        print("===========================================")
        print("welcome to system cinema control manager")
        print("===========================================")
        print("[ 1 ] View movie")
        print("[ 2 ] Add New movie")
        print("[ 3 ] Add Cart to pay")
        print("[ 4 ] Remove the movie")
        print("[ 5 ] Manage Users")
        print("[ 6 ] View history")
        print("[ 7 ] Clear history all data")
        print("[ 8 ] logout")
        choice = input("select the option:")

        if choice == '1':
            manager_cashier.view_data()
            continues()

        elif choice == '2':
            adds = input("enter movie name:")
            while True:
                try:
                    hours = int(input("enter hours 1hr-12hr:"))
                    if hours <= 12 :
                       print(f"{hours} hr : XX min")
                    elif hours > 12 or hours == 0 :
                       print("it not a time!!")
                       break
                    minute = int(input("enter minute 00min - 60min:"))
                    if minute < 60 :
                        print(f"{hours}hr : {minute:02d}min")
                    elif minute >= 60  or hours == 0:
                        print("it not a time!!")
                        break
                    pal = input("enter AM or PM:").upper()
                    if pal == 'am' and pal == 'pm':
                       pass
                    elif pal != 'AM' and pal != 'PM':
                        print("it not a time!!")
                        break
                    times = f"{hours}:{minute:02d} {pal}"
                    prices = float(input("enter price $ per 1 ticket:"))
                    manager_cashier.add_movie(add=adds,time=times,price=prices)
                    continues()
                    break
                except ValueError:
                    print("wrong value!!")

        elif choice == '3':
            while True:
                space = []
                manager_cashier.view_data()
                how_many, choose = manager_cashier.payment()
                g = manager_cashier.check_outs1()
                if g == 0:
                    continues()
                    break
                for i in range(how_many):
                    while True:
                        try:
                            seat = int(input("Enter seat number from 1-100: "))
                            if seat <= 100:
                                data = client.saving()
                                already_book = any(
                                    e['seat'] == seat and e['hall'] == choose
                                    for e in data
                                )
                                if already_book:
                                    print("‼️ This seat has been book by someone in this hall")
                                else:
                                    client.enter_data(seat=seat, halls=choose, user=user)
                                    space.append(seat)
                                    print(f"✅ Your seat booking [hall {choose} - seat {seat}] is confirm")
                                    break
                            elif seat > 100:
                                print("our hall dont have 100 up seat sorry")
                        except ValueError:
                            print("It's not a number!!")
                user += 1
                print(f"Your seats : {space} , in hall  {choose} Thank you! ")
                for i in range(10):
                    sys.stdout.write("\rwaiting 5 second to create PDF" + "." * (i % 6))
                    sys.stdout.flush()
                    time.sleep(0.5)
                print("\nDone!!")
                mainss()
                continues()
                break

        elif choice == '4':
            manager_cashier.view_data()
            t = int(input("1/to remove movie , 2/to clear all movie:"))
            if t == 1:
                try:
                    deletes = int(input("enter HALL to remove:"))
                    manager_cashier.removing(delete=deletes)
                    continues()
                except ValueError:
                    print("please enter valid ID")
                    continues()

            elif t == 2:
                conform = input("are you sure you want to clear all data movie (y or n):")
                if conform == 'y':
                    manager_cashier.clear_movie()
                    print("movie has been clear all from the data")
                    continues()
                elif conform == 'n':
                    print("ok !!")
                    continues()
                else:
                    print("please enter Y or N")
                    continues()
            else:
                print("wrong choice!! please try again")
                continues()

        elif choice == '5':
            print("*" * 40)
            login_security.view_manager()
            print("*" *40)
            print("a. for add more ")
            print("b. back ")
            a = input("enter :")
            if a == 'a':
               login_security.registered()
               continues()
            if a == 'b':
                break
            continues()

        elif choice == '6':
            manager_cashier.history()
            continues()

        elif choice == '7':
            sure = input("Are you sure you want to clear all data(y or n)?:")
            if sure.lower() == 'y':
               manager_cashier.clear_data()
               client.clear_datas()
               print("your data have been clear .")
               continues()
            else:
               print("Thank you!")
               continues()

        elif choice == '8':
            print("Thank you for using Cinema system !")
            break
        else:
            input("press number from 1 - 7 ...")

def main():
    while True:

        me = login_security.manage_cashiers()
        if me == 'cashier':
           cashiers()
        elif me == 'manager':
           managers()
if __name__ == '__main__':
    main()
