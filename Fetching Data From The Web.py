import requests

key = 'f93ced4'

baseURL = 'http://www.omdbapi.com/'

movie = input("Enter a movie to search for: \n")

parameters = { 'apikey' : key, 't' : movie}

data = requests.get(baseURL, parameters ).json()

print(data)