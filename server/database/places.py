import json 
import requests as r
from connection import Connection
# import os

con = Connection()

# API_KEY = os.environ["PLACES_API_KEY"]
API_KEY = "AIzaSyAgFaxKO-dDZwjWGLvjlKrhGd6uLStEElY"
baseURL = "https://maps.googleapis.com/maps/api/place/textsearch/json"

names = con.retrive("SELECT * from Names")

for name in names:

  para = {'key':API_KEY,'query':name[1]}
  data = r.get(baseURL,para).json()
  print(data)

  for result in data['results']:
    
    sql = "insert into places (place_id,name,lat,lng,type,state) values {}".format(tuple((result['place_id'],result['name'],float(result['geometry']['location']['lat']),float(result['geometry']['location']['lng']),result['types'][0],'Rajasthan')))
    try:
      con.insert(sql)
    except:
      pass
    # result['type'][0]

