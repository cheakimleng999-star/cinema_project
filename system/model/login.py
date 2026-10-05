import json
class Login:
    def __init__(self):
        self.cookie = []
        self.file = 'system/database/datas.json'
        self.loading()
    def register(self,username,password,note):
        data = {
            'username' : username,
            'password' : password,
            'users'    : note
        }

        self.cookie.append(data)
        self.saving()

    def logins(self,username,password):
        for i in self.cookie:
            if i['username'] == username and i['password'] == password:
                return True
        return False

    def view_manager(self):
        for i in self.cookie:
            print(f"{i['username']} , ===> {i['users']}")

    def saving(self):
        with open(self.file, 'w') as f:
            json.dump(self.cookie, f, indent=4)

    def loading(self):
        try:
            with open(self.file, 'r') as f:
                self.cookie = json.load(f)
            return self.cookie[0]['users']
        except (FileNotFoundError, json.JSONDecodeError):
            self.cookie = []

    def manage_cashiers(self):
        print("============Welcome to manage cinema============")
        username = input("login username:")
        password = input("login password:")
        if self.logins(username, password):
            for i in self.cookie:
                if i['username'] == username and i['password'] == password:
                    print(f"login successful")
                    return i['users']
        print("login failed")
        return False

    def registered(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        while True:
            note = input("Enter are you manager or cashier: ")
            if note == 'manager' or note == 'cashier':
                self.register(username, password, note)
                print("register successful")
                break
            else:
                print("please enter full world")
