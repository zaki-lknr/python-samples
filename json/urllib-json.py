import urllib.request
import ssl
import json

context = ssl._create_unverified_context()

req = urllib.request.Request('https://api.example.org/api/')
with urllib.request.urlopen(req, context=context) as res:
    d = json.load(res)

print(d)
