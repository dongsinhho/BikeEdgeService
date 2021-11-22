import requests
import random
from time import sleep

id = 1
URL_API = "http://127.0.0.1:8000/api/bikes/{}/".format(id)

def SendData():
    while True:
        latitude = random.uniform(10.870000, 10.880000)
        longtitude = random.uniform(106.780000,106.800000)
        
        latitude = str(format(round(latitude,6)))
        longtitude = str(format(round(longtitude,6)))
        data = {
                "latitude": latitude,
                "longtitude": longtitude
            }
        print(data)
        requests.post(URL_API, data=data)
        sleep(3)
if __name__ == "__main__":
    SendData()
    