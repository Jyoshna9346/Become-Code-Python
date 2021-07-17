class CricketTeam:
    country="INDIA"
    def __init_(self,teamname,nm):
        self.teamname=teamname
        self.nm=nm
    def display(self):
        print(self.teamname,self.nm)
        
class Batsman(CricketTeam):
    def __init__(self,teamname,nm,name,hs,runs,sr,avg,age):
        self.name=name
        self.runs=runs
        self.sr=sr
        self.avg=avg
        self.age=age
        self.hs=hs
    def display(self):
        print(self.name,self.runs,self.sr,self.hs,self.avg,self.age)
b1=Batsman("RCB","90","VIRAT",200,7500,134.3,43.2,31)
b1.display()
           
'''VIRAT 7500 134.3 200 43.2 31 '''

class CricketTeam:
    country="INDIA"
    def __init_(self,teamname,nm):
        self.teamname=teamname
        self.nm=nm
    def display(self):
        print(self.teamname,self.nm,Batsman.country)
        
class Batsman(CricketTeam):
    country="india"
    def __init__(self,teamname,nm,name,hs,runs,sr,avg,age):
        super().__init__(teamname,nm)
        self.name=name
        self.runs=runs
        self.sr=sr
        self.avg=avg
        self.age=age
        self.hs=hs
    def display(self):
        super().display()
        print(self.name,self.runs,self.sr,self.hs,self.avg,self.age,self.country)#super().country
b1=Batsman("RCB","90","VIRAT",200,7500,134.3,43.2,31)
b1.display()
