import requests
import json
import pymongo
import pandas as pd

# try:
#     client = pymongo.MongoClient()
#     print("Connected successfully!!!")
# except:
#     print("Could not connect to MongoDB")
#Connect to starwars API
response_API = requests.get('https://swapi.dev/api/starships')
print(response_API.status_code)

data = response_API.json()
print(data)

#loop through data. look for next page in 'next'
