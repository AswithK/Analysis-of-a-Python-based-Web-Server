import requests
r = requests.get('http://127.0.0.2:80/cn_text.txt')
print(r.text)
