import requests
r = requests.get('http://127.0.0.2:80/')
print(r.text)
