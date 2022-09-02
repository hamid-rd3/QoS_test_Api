from logging import exception
import requests
from getpass import getpass
import yaml
auth_endpoint = "http://localhost:5201/api/auth/"
password = getpass()

auth_token = requests.post(
    url=auth_endpoint, json={"username": "hamidrd11", "password": password})

if auth_token.status_code == 200:
    token = auth_token.json()['token']
    headers = {
        'Authorization': f"Bearer {token}",
    }
else:
    raise exception("password is wrong ")
endpoint = "http://localhost:5201/api/products/"

with open('config.yaml', 'r') as config:

    data = yaml.full_load(config)

get_responce = requests.post(url=endpoint, headers=headers, json=data)

print(get_responce.status_code, get_responce.json())
