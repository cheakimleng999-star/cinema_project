from system.model.staff import Client
from system.model.manager_cashier import Manager
from system.model.login import Login
from system.model.pdf_ticket import *
import time


login_security = Login()
manager_cashier = Manager()
client = Client()

def continues():
    input("Try any key to be continue.....")

def cashiers():
    user = 1
    while True:
        print("[ 1 ] View movie")
        print("[ 2 ] Add Cart to pay")
        print("[ 3 ] Remove the movie")
        print("[ 4 ] logout")
        choice = input("select the option:")

        if choice == '1':
            manager_cashier.view_data()
            continues()

        elif choice == '2':
            manager_cashier.view_data()
            how = manager_cashier.payment()

            if how == 0:
                break
            g = manager_cashier.check_outs1()

            if g == "wrong":
                break
            # To put payment total
            for i in range(how):
                while True:
                    try:
                        seat = int(input("Enter seat number from 1-100: "))
                        data = client.saving()
                        booking = [
                            e['seat']
                            for e in data
                        ]

                        if seat in booking:
                            print("‼️ This seat has been book by someone")
                        else:
                            client.enter_data(seat, user)
                            print(f"✅ Your seat booking [{seat}] now")
                            break
                    except ValueError:
                        print("it not a number!!")
            data = client.saving()
            user_seat = [
                e['seat']
                for e in data
                if e['user'] == user
            ]
            print("Your seats:", ",".join(f"[{seat}]" for seat in user_seat))
            user += 1
            print("please waiting 5 ......")
            time.sleep(5)
            mainss()
            continues()

        elif choice == '3':
            manager_cashier.view_data()
            try:
                deletes = int(input("enter ID to remove:"))
                manager_cashier.removing(delete=deletes)
                continues()
            except ValueError:
                print("please enter valid ID")
                continues()
        elif choice == '4':
            break

def managers():
    user = 1
    while True:
        print("[ 1 ] View movie")
        print("[ 2 ] Add New movie")
        print("[ 3 ] Add Cart to pay")
        print("[ 4 ] Remove the movie")
        print("[ 5 ] Manage Users")
        print("[ 6 ] View history")
        print("[ 7 ] logout")
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
                       print(f"{hours}hr : XXmin")
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
                    print("wrong Value!!")
        elif choice == '3':
            manager_cashier.view_data()
            how = manager_cashier.payment()

            if how == 0:
                continues()
                break
            g = manager_cashier.check_outs1()

            if g == 0:
                continues()
                break


            for i in range(how):
                while True:
                    try:
                        seat = int(input("Enter seat number from 1-100: "))
                        data = client.saving()
                        booking = [
                            e['seat']
                            for e in data
                        ]

                        if seat in booking:
                            print("‼️ This seat has been book by someone")
                        else:
                            client.enter_data(seat, user)
                            print(f"✅ Your seat booking [{seat}] now")
                            break
                    except ValueError:
                        print("it not a number!!")
            data = client.saving()
            user_seat = [
                e['seat']
                for e in data
                if e['user'] == user
            ]
            print("Your seats:", ",".join(f"[{seat}]" for seat in user_seat))
            user += 1
            print("please waiting 5 ......")
            time.sleep(5)
            mainss()

            continues()

        elif choice == '4':
            manager_cashier.view_data()
            try:
                deletes = int(input("enter ID to remove:"))
                manager_cashier.removing(delete=deletes)
                continues()
            except ValueError:
                print("please enter valid ID")
                continues()
        elif choice == '5':
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