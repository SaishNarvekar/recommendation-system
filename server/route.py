from server.connection import Connection
from server.model import Model
from server.util import Util
import csv

con = Connection() #database Connection 
model = Model()
util = Util()


class Route:

    def __init__(self,startPoint,days,prefernce,state):
        
        self.days = days
        self.userPreference = prefernce
        self.starting = startPoint
        self.state = state
        self.filterLocation(prefernce,state) #fliter Location based on user location
        
    def filterLocation(self,userPreference,state):

        if self.state == 'Goa':

            if 'Beach' in userPreference:
                sql = "select * from places where state = '{}' and type in {} and Rating >= 4.0 UNION select * from places where name = '{}' UNION select * from places where name = '{}'".format(self.state,tuple(userPreference),'Vasco da Gama','Colva Beach')
            else:
                sql = "select * from places where state = '{}' and type in {} UNION select * from places where name = '{}' UNION select * from places where name = '{}'".format(self.state,tuple(userPreference),'Vasco da Gama','Colva Beach')

        if self.state == 'Rajasthan':
            sql = "select * from places where state = '{}' and Rating >= 4.5 and type in {} UNION select * from places where name = 'Jaswant Thada' UNION select * from places where name = 'Jaigarh Fort'".format(self.state,tuple(userPreference))

        cur = con.retrive(sql)
        # print(cur)
        with open('.\\server\\files\\filter.csv', 'w+') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for row in cur:
                filewriter.writerow(list(row))
    
    def GameOver(self):

        locations = list()
        visitedLocation = list()

        for index in model.filterPlaces(self.starting):
            locations.append(index)

        # print(locations)
    
        locations.remove(self.starting)
        visitedLocation.append(self.starting)
        placesVisited = 1

        while placesVisited != int(self.days)*3:
            if len(locations) == 0:
                break 
            close = util.findClosestLocation(visitedLocation[-1],locations)
            # print(close)
            locations.remove(close)
            visitedLocation.append(close)
            placesVisited+=1
        return visitedLocation