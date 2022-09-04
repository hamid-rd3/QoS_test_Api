
import requests
from getpass import getpass
from requests_toolbelt.multipart.encoder import MultipartEncoder

auth_endpoint = "http://localhost:5201/api/auth/"
password = getpass()

mp_encoder = MultipartEncoder({"username": "hamid", "password": password})
auth_token = requests.post(
    url=auth_endpoint, data=mp_encoder, headers={'Content-type': mp_encoder.content_type})


if auth_token.status_code == 200:
    token = auth_token.json()['token']
    headers = {
        'Authorization': f'Bearer {token}',
    }
    endpoint = "http://localhost:8000/api/products/"
    get_responce = requests.get(url=endpoint, headers=headers)

print(get_responce.status_code, get_responce.json())
