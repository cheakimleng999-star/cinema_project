from datetime import datetime
import random
import json

class Client:
    def __init__(self):
        self.json = 'system/database/client.json'
        self.datas = []

    def enter_data(self , seat ,user):
        data = {
            'user':user,
            'id'  : random.randint(1000,9999)   ,
            'seat': seat  ,
            'time': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.datas.append(data)
        self.saving()
        return  data['seat']

    def saving(self):
        with open(self.json,'w') as f:
            json.dump(self.datas,f,indent=4)
        return self.datas

