from logging import exception
import requests
from getpass import getpass
import yaml
from requests_toolbelt.multipart.encoder import MultipartEncoder

auth_endpoint = "http://localhost:8000/api/auth/"
password = getpass()

mp_encoder = MultipartEncoder({"username": "hamid", "password": password})
auth_token = requests.post(
    url=auth_endpoint, data=mp_encoder, headers={'Content-type': mp_encoder.content_type})


if auth_token.status_code == 200:
    token = auth_token.json()['token']
    headers = {
        'Authorization': f"Bearer {token}",
    }
else:
    raise exception("password is wrong ")
endpoint = "http://localhost:8000/api/products/"

# with open('config.yaml', 'r') as config:

#     data = yaml.full_load(config)

get_responce = requests.post(url=endpoint, headers=headers, json={
"site_url": "https://www.varzesh3.com/",
"ping_count" : 5,
"ping_timeout" : 0.2,
"ping_algorithm" : "binary_search",
"ddosify_count" : 100,
"ddosify_duration" : 5,
"ddosify_timeout" : 1,
"async_view" : True})

print(get_responce.status_code, get_responce.json())
