import requests

x = requests.post('http://127.0.0.1:5000/dataentry')
print(x.content)

