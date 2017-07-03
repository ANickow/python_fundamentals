import requests

r = requests.get('http://ron-swanson-quotes.herokuapp.com/v2/quotes')

print r.text
