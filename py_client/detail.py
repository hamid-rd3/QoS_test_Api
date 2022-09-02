import requests

endpoint = "http://localhost:8000/api/products/3/"
headers = {'Authorization': f'token 8dd00f4e0a7494551ffaead8d06f65f4cccf3a6a'}
get_responce = requests.get(url=endpoint, headers=headers)

print(get_responce.status_code, get_responce.json())
