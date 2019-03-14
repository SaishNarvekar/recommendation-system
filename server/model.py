import numpy as np
import pandas as pd

class Model:
    
    def __init__(self):
        pass

    def filterPlaces(self,starting):
        self.poi= pd.read_csv('filter.csv',index_col='Name',names = ['placeID','Name','Lat','Lng','Rating','Type'])
        self.reviews = pd.read_csv('reviews.csv',index_col='Name',names=['ID','Name','UserID','UserRating'])
        self.poi.drop(columns=['placeID','Lat','Lng'],axis=1,inplace=True)
        self.reviews.drop(columns=['ID'],axis=1,inplace=True)
        self.overall = self.poi.join(self.reviews,on='Name')
        self.overall_pvtable = self.overall.pivot_table(index='UserID',columns='Name',values='UserRating')
        print(self.poi)
        # print(starting)
        self.startingLocation = self.overall_pvtable[starting]
        self.similarToStarting = pd.DataFrame(self.overall_pvtable.corrwith(self.startingLocation),columns=['Correlation'])
        self.similarToStarting.dropna(inplace=True)
        self.similarToStarting.sort_values(by='Correlation',ascending=False)
        self.recommendedLocation = self.similarToStarting.join(self.poi,on='Name').sort_values(by='Rating',ascending=False)
        return self.recommendedLocation.index