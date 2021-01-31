import json
import requests
from datetime import date
import pandas as pd

url = "https://certificationapi.oshwa.org/api/projects"

f = open("apiKey.txt", "r")
payload = {}
headers = {
    'Content-Type': 'application/json',
    'Authorization': ('Bearer '+f.readline())
}
f.close() 
response = requests.request("GET", url, headers=headers, data=payload)
if(response.status_code == 200):
    pdObj = pd.read_json(response.content, orient='records')
    csvData = pdObj.to_csv('oshwa_api_' + str(date.today()) + '.csv', index=False)
    print("Write successful")
elif(response.status_code == 401):
    print("Invalid API key")
else:
    print("Unknown error. Response code: " + response.status_code)
