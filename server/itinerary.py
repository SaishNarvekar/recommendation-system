from route import Route


class Itinerary:

    def __init__(self,travelType,days,prefernce):

        self.travelType = travelType
        self.days = days
        self.prefernce = prefernce
        self.output = {}

    def getItinerary(self):

        i  = 0

        if self.travelType == 'Airway':

            route = Route('Vasco da Gama',self.days,self.prefernce) #List will get created by user and filled with data from front end
            itinerary = route.GameOver()
            self.output[i] = itinerary
            return self.output

        if self.travelType == 'Railway':

            route = Route('Vasco da Gama',self.days,self.prefernce)
            itinerary = route.GameOver()
            self.output[i] = itinerary
            
            i+=1

            route = Route('Colva Beach',self.days,self.prefernce) #List will get created by user and filled with data from front end
            itinerary = route.GameOver()
            self.output[i] = itinerary
            
            return self.output
            
