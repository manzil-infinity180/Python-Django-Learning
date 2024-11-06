import requests

endpoints = 'http://localhost:8000/api'

get_response = requests.post(endpoints, json={"title": "coming from json query"})
print(get_response.json())
print(get_response.status_code)