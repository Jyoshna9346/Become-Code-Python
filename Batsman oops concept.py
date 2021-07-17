class Batsman:
    teamname="INDIA BLUE"
    def __init__(self,name,m,hs,runs,sr,bf,avg,age):
        self.name=name
        self.m=m
        self.runs=runs
        self.sr=sr
        self.bf=bf
        self.avg=avg
        self.age=age
        self.hs=hs
        self.teamname="India Red"
    def display(self):
        print(self.name,self.m,self.runs,self.sr,self.bf,self.avg,self.age,self.teamname)
    
b1=Batsman("arjun",200,110,7500,82.3,12000,43.2,31)
b1.display()
b2=Batsman("arun",200,110,7500,82.3,12000,43.2,31)
b2.display()

arjun 200 7500 82.3 12000 43.2 31 India Red
arun 200 7500 82.3 12000 43.2 31 India Red
