import requests
import json
import os


accountSID = "acce76c9324-1b7c-36a5-8e00-ed83be6c2043"
numSID = "num6eb8d7d5-6bbb-3249-a341-2271986ce567"
url = "https://api.apifonica.com/v2/accounts/" + accountSID


## link the application to apifonica
messagesURL = url + '/messages'
head = {"Content-Type": "application/json"}
authorise = ("acce76c9324-1b7c-36a5-8e00-ed83be6c2043", "aut0eac9ad3-ee88-3f3f-8664-e0bc1dd60cc8")

#getAppsResponse = requests.get()

response = requests.get(messagesURL, headers=head, auth=authorise)
print(response.text)