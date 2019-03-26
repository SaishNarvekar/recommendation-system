import json 
import requests as r
from connection import Connection

con = Connection()

baseURL = "https://maps.googleapis.com/maps/api/place/details/json"
API_KEY = "AIzaSyAgFaxKO-dDZwjWGLvjlKrhGd6uLStEElY"

places_ids = con.retrive("SELECT place_id from places where state = 'Rajasthan'")

for pid in places_ids:
    pid = pid[0]
    para = {'key':API_KEY,'placeid':pid}
    # print(para)

    data = r.get(baseURL,para).json()

    print(data)

    name = data['result']['name']
    if 'rating' in data['result']:
        overallRating = data['result']['rating']
    else:
        overallRating = 0

    sql = "update places set rating = {} where place_id = \"{}\"".format(overallRating,pid)
    con.insert(sql)

    if 'reviews' in data['result']:
        for review in data['result']['reviews']:
            author_name = review['author_name']
            rating = review['rating']
            sql = "insert into reviews(name,author_name,rating) values {}".format(tuple((name,author_name,rating)))
            print(sql)
            con.insert(sql)

    fileName = "files\\{}.txt".format(name)

    fp = open(fileName,'w')

    for category in data['result']['types']:
        print(category)
        fp.write(category)
        fp.write('\n')

    # categories = data['result']['types']
    # sql = "insert into categories values {}".format(tuple((pid,name,categories)))
    # print(sql)
    fp.close()