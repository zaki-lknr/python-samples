import requests

r = requests.get('https://192.168.0.12:6443/api/v1', verify=False)
print(r.json())
