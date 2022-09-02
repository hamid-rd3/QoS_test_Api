import requests

endpoint = "http://localhost:8000/api/products/1/delete/"

get_responce = requests.delete(url=endpoint)

print(get_responce.status_code)
