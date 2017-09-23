import requests
import json
import os


accountSID = "acce76c9324-1b7c-36a5-8e00-ed83be6c2043"
numSID = "num6eb8d7d5-6bbb-3249-a341-2271986ce567"
url = "https://api.apifonica.com/v2/accounts/" + accountSID


## make an application


## link the application to apifonica
applicationURL = url + '/applications'
head = {"Content-Type": "application/json"}
data = {
    "controller": "http://172.19.26.58:3000/message",
    "method": "POST",
    "name": "App1"
}
authorise = ("acce76c9324-1b7c-36a5-8e00-ed83be6c2043", "aut0eac9ad3-ee88-3f3f-8664-e0bc1dd60cc8")

#getAppsResponse = requests.get()

response = requests.post(applicationURL, headers=head, data=json.dumps(data), auth=authorise)

print('sent application to apifonica')
print(response.text)
j = json.loads(response.text)
applicationSID = j['uri'].split('/')[-1]

## link the application to the phone number
numberURL = url + '/numbers/' + numSID
data2 = {
    "msg_app_sid": applicationSID
}
response = requests.put(url, headers=head, data=json.dumps(data2), auth=authorise)
print('linked application ID to apifonica number')
print(response.text)
