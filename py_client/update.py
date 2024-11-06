import requests

endpoints = 'http://localhost:8000/api/products/3/update/'


get_response = requests.patch(endpoints, json={"title": "Hey beautiful"})
print(get_response.json())
print(get_response.status_code)