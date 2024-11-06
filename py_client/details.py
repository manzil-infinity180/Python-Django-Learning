import requests
from getpass import getpass
endpoints_auth = 'http://localhost:8000/api/auth/'
password = getpass("Enter your password ?")
get_response_auth =  requests.post(endpoints_auth, json={"username":"admin", "password": password})


print(get_response_auth.json())

endpoints = 'http://localhost:8000/api/products/3/'

if get_response_auth.status_code == 200:
    token = get_response_auth.json()['token']
    # get_response = requests.get(endpoints, headers={"Authorization": f"Token {token}"})
    get_response = requests.get(endpoints, headers={"Authorization": f"Bearer {token}"})
    print(get_response.json())
    print(get_response.status_code)