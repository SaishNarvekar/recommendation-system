from server.route import Route
from server.connection import Connection


class Itinerary:

    def __init__(self,travelType,days,prefernce,state):

        self.travelType = travelType
        self.days = days
        self.prefernce = prefernce
        self.state = state
        self.output = {}
        self.con = Connection()

    def getItinerary(self):

        i  = 0

        if self.state == 'Goa':

            if self.travelType == 'Airway':

                route = Route('Vasco da Gama',self.days,self.prefernce,self.state) #List will get created by user and filled with data from front  end
                itinerary = route.GameOver()
                self.output[i] = self.formatedOutput(itinerary)
                return self.output

            if self.travelType == 'Railway':

                route = Route('Vasco da Gama',self.days,self.prefernce,self.state)
                itinerary = route.GameOver()
                self.output[i] = self.formatedOutput(itinerary)

                i+=1

                route = Route('Colva Beach',self.days,self.prefernce,self.state) #List will get created by user and filled with data from front end
                itinerary = route.GameOver()
                self.output[i] = self.formatedOutput(itinerary)

                return self.output

        if self.state == 'Rajasthan':

            if self.travelType == 'Airway':

                route = Route('Jaswant Thada',self.days,self.prefernce,self.state) #List will get created by user and filled with data from front  end
                itinerary = route.GameOver()
                self.output[i] = self.formatedOutput(itinerary)
                return self.output

            if self.travelType == 'Railway':

                route = Route('Jaigarh Fort',self.days,self.prefernce,self.state)
                itinerary = route.GameOver()
                self.output[i] = self.formatedOutput(itinerary)

                return self.output

    def formatedOutput(self,itinerary):
        formatedItinerary = list()
        for i in itinerary:
            op = {}
            lat,lng = self.getLatLong(i)
            op['name'] = i
            op['lat'] = lat
            op['lng'] = lng
            formatedItinerary.append(op)
        return formatedItinerary


    def getLatLong(self,location):
        sql = 'select lat,lng from places where name = "{}"'.format(location)
        cur = self.con.retrive(sql)
        for row in cur:
            pass
        return row[0],row[1]
        
            
