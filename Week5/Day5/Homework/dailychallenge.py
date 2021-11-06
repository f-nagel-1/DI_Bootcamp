import requests

response = requests.get('http://google.com/').elapsed.total_seconds()

print(response)

