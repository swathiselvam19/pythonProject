import requests
import json

response = requests.get('http://216.10.245.166/Library/GetBook.php',params={'AuthorName':'RAJANIKANTH'})

print(response.text)

