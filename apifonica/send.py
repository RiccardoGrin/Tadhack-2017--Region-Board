import requests
import json
import os

SID = "acce76c9324-1b7c-36a5-8e00-ed83be6c2043"
url = "https://api.apifonica.com/v2/accounts/" + SID + "/messages"

data = {
    "from": "61476857588",
    "to": "61490761724",
    "text": "Apifonica API provides a really cool SMS messaging service"
}

head = {"Content-Type": "application/json"}

authorise = ("acce76c9324-1b7c-36a5-8e00-ed83be6c2043", "aut0eac9ad3-ee88-3f3f-8664-e0bc1dd60cc8")

response = requests.post(url, headers=head, data=json.dumps(data), auth=authorise)

print(response.text)