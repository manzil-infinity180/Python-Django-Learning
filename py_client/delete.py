import requests

endpoints = 'http://localhost:8000/api/products/4/delete/'


get_response = requests.delete(endpoints)
print(get_response.status_code,get_response.status_code==204 )