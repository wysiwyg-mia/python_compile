import json
import requests
import time

class Req:
    def req(data):
        try:
            payload = {
                "fio": data[0],
                "resultDate": data[1],
                "dob": data[2],
                "sex": 0 if data[3] == "M" else 1,
                "phone": data[4],
                "organization": data[5],
                "medCenter": data[6],
                "address": data[7],
                "verificationId": 1,
                "path": data[9]
            }
            time.sleep(3)
            r = requests.post('http://0.0.0.0:3000/api/v2/images/mashina', json=payload)
            return True
        except Exception as e:
            return False