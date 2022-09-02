
import requests
from getpass import getpass

auth_endpoint = "http://localhost:8000/api/auth/"
password = getpass()

#
auth_token = requests.post(
    url=auth_endpoint, json={"username": "hamid", "password": password})


if auth_token.status_code == 200:
    token = auth_token.json()['token']
    headers = {
        'Authorization': f'token {token}',
    }
    endpoint = "http://localhost:8000/api/products/"
    get_responce = requests.get(url=endpoint, headers=headers)

print(get_responce.status_code, get_responce.json())
