import requests

endpoint = "http://localhost:8000/api/products/5/update/"

data = {"site_url": "https://www.yasdl.com/",
        "count": 1, "algorithm": "binary_search"}
get_responce = requests.put(url=endpoint, json=data)

print(get_responce.status_code, get_responce.json())
