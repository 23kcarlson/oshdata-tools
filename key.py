import requests
import json
import sys
url = "https://certificationapi.oshwa.org/users/signup"
if(len(sys.argv)==4):
    payload = "{\"firstName\": \""+sys.argv[1]+"\",\"lastName\": \""+sys.argv[2]+"\",\"email\": \""+sys.argv[3]+"\"}"
elif(len(sys.argv)==1):
    payload = "{\"firstName\": \""+input("First Name: ")+"\",\"lastName\": \""+input("Last Name: ")+"\",\"email\": \""+input("Email: ")+"\"}"
else:
    print("Usage: key.py firstName lastName email@example.com")
    print("Usage: key.py")
    exit()

headers = {
    'Content-Type': 'application/json',
}
response = requests.request("POST", url, headers=headers, data=payload)
if(response.status_code == 201):
    f = open("apiKey.txt", "w")
    f.write(json.loads(response.text.encode('utf8'))["token"])
    f.close()   
    print("API key created")
elif(response.status_code == 422):
    print("Invalid field(s)")
else:
    print("Unknown error. Response code: " + response.status_code)