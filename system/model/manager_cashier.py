import json
import csv
import random
from datetime import datetime
class Manager:
    def __init__(self):
        self.csv = "data_" + str(random.randint(1, 100)) + ".csv"
        self.movie_name = []
        self.check_out = []
        self.file = 'system/database/movie_data.json'
        self.file1 = 'system/database/total_payment.json'
        self.loading()
        self.loading1()
        self.id = 1
    def add_movie(self, add,time,price):
        if self.movie_name:
            self.id = max(i['ID'] for i in self.movie_name) + 1
        else:
            self.id = 1
        data = {
            'ID'        : self.id,
            'movie_name': add,
            'time_start': time,
            'price'     : price,

        }
        self.movie_name.append(data)
        self.saving()
        print("adding successfully")

    def view_data(self):
        print(f"{'num':<5}{'HALL':<5}{'movie_name':<25}{'time start':<15}{'price':>10}")
        print("-" * 55)
        for number, i in enumerate(self.movie_name, start=1):
            print(f"{number:<5}HALL:{i['ID']:<5}{i['movie_name']:<25}{i['time_start']:<15}${i['price']:>10}  per ticket")
        print("-" * 55)
        return True

    def removing(self,delete):
        for i in self.movie_name:
            if i['ID'] == delete:
                self.movie_name.remove(i)
                print("removing successfully")
                self.saving()
                return
        print(f"fail remove dont have in your data")

    def payment(self):
        while True:
            try:
                choose = int(input("enter movie [HALL] you want to enjoy :"))
                for i in self.movie_name:

                    if choose == i['ID']:
                       how_many = int(input("how many seats you want:"))
                       print(f"{how_many}X of movie {i['movie_name']} to cart. ")
                       total  = i['price'] * how_many
                       wu = {
                           'name_movie' : i['movie_name'],
                           'hall' : choose,
                           'how_many': how_many,
                           'total' : total,
                           'date_total' : datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                           'pay_done' : False
                       }
                       self.check_out.append(wu)
                       with open(self.file1,'w') as f:
                           json.dump(self.check_out,f , indent=4)
                           self.check_outs()
                       return how_many , choose
                print("fail payment dont have in your data")
            except ValueError:
                print("enter wrong value")

    def check_outs(self) :
        i = self.check_out[-1]
        print(f"{'Movie_name':<20}{'Qty':<30}{'Total':<15}")
        print("-" * 55)
        print(f"{i['name_movie']:<20}{i['how_many']:<30}${i['total']:>15}")
        print(f"\nTotal: ${i['total']}\n")

    def check_outs1(self):
        while True:
            try:
                i = self.check_out[-1]
                confirm = input("do you want to pay? (y/n):")
                if confirm == 'y':
                    i['pay_done'] = True
                    self.saving1()
                    print("payment successfully")
                    return 1
                elif confirm == 'n':
                    i['pay_done'] = False
                    self.saving1()
                    print("payment fail")
                    break
                else:
                    print("enter wrong value")

            except IndexError :
                print(f"NO DATA FOUND")

    def history(self):

        print(f"{'name_movie':<20}{'ticket':<20}{'total':<20}{'date':<10}")
        print("-" * 80)
        for i in self.check_out:
            status = "✅ pay done" if i['pay_done'] else "‼️ not done"
            print(
                f"{i['name_movie']:<20}"
                f"{i['how_many']:<20}"
                f"${i['total']:<20}"
                f"{i['date_total']:<10}"
                f"[{status}]"

            )
        print("-" * 80)
        print(f"all ToTal :{sum(i['total'] for i in self.check_out)}    $")
        print("\n")
        o = input("do you want CSV file? (y/n):")
        if o == 'y':
            with open(self.csv , "w",newline="") as p:
                w = csv.writer(p)
                w.writerow(["name_movie", "ticket" , "total" , "date" , "paying"])
                for i in self.check_out:
                    w.writerow([
                        i["name_movie"],
                        i["how_many"],
                        f"{i["total"]}$",
                        i["date_total"],
                        i["pay_done"]
                    ])
                print(f"save done! file: {self.csv}")
        else:
            print("ok !")

    def saving(self):
        with open (self.file, 'w') as f:
            json.dump(self.movie_name, f , indent=4)


    def saving1(self):
        with open (self.file1, 'w') as f:
            json.dump(self.check_out, f , indent=4)

    def loading(self):
        try:
            with open (self.file, 'r') as f:
                self.movie_name = json.load(f)
        except (FileNotFoundError , json.decoder.JSONDecodeError) :
            self.movie_name = []

    def loading1(self):
        try:
            with open (self.file1, 'r') as f:
                self.check_out = json.load(f)
        except (FileNotFoundError , json.decoder.JSONDecodeError):
            self.check_out = []

    def clear_data(self):
        self.check_out = []
        with open(self.file1 , "w") as g:
            json.dump([] , g)
