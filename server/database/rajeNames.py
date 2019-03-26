from connection import Connection
import requests as r
import re
import bs4 as bs

con = Connection()
    
BaseURL = 'http://www.tourism.rajasthan.gov.in/'
URLS = ['tourist-destinations.html','forts.html','palaces-to-visit.html','museums-to-visit.html','lakes-rivers-to-visit.html','religious-places.html','parks-and-wildlife.html']
# URLS = ['tourist-destinations.html']
    
for url in URLS:
    req = r.get(BaseURL+url)
    soup = bs.BeautifulSoup(req.text,'lxml')
    data = soup.select('.innerTitle > p')
    data = list(map(lambda x : x.text,data))
    for i in data:
        sql = "insert into names (name) values ('{}');".format(re.sub(r'\'','',i))
        print(sql)
        con.insert(sql)
