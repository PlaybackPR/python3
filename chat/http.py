import requests
response = requests.get('https://wttr.in')
print(response.text)