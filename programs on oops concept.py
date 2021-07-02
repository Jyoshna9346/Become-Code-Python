'''
class student:
    def __init__(self,rollno,name,branch,per,bc):
        self.rollno=rollno
        self.name=name
        self.branch=branch
        self.per=per
        self.bc=bc
    def displaydata(self):
        print(self.rollno,self.name,self.branch,self.per,self.bc)
std1=student("123","jyoshna","ece","79",0)#object creation
std1.displaydata()
std2=student("124","manasa","ece","56",0)#object creation
std2.displaydata()

ouput:
123 jyoshna ece 79 0
124 manasa ece 56 0

'''
'''
class student:
    college="ADITYA"
    def __init__(self,rollno,name,branch,per,bc):
        self.rollno=rollno
        self.name=name
        self.branch=branch
        self.per=per
        self.bc=bc
        self.college="aditya"
    def displaydata(self):
        print(self.rollno,self.name,self.branch,self.per,self.bc)
    def fun(self,a,branch):
        print(a,branch)
std1=student('124','jyoshna','ece','99',0)
std1.displaydata()
std2=student("123","manasa","ece","77",0)
std2.displaydata()
'''

#batsman
'''
class Batsman:
    def __init__(self,name,m,hs,runs,sr,bf,avg,age):
        self.name=name
        self.m=m
        self.runs=runs
        self.sr=sr
        self.bf=bf
        self.avg=avg
        self.age=age
        self.hs=hs
    def display(self):
        print(self.name,self.m,self.runs,self.sr,self.bf,self.avg,self.age)
b1=Batsman("virat",200,110,75000,86.5,12000,43.5,31)
b1.display()


virat 200 75000 86.5 12000 43.5 31
'''
#same program then above little changes..include somemore info

'''
class Batsman:
    teamname="INDIA Blue" 
    def __init__(self,name,m,hs,runs,sr,bf,avg,age):
        self.name=name
        self.m=m
        self.runs=runs
        self.sr=sr
        self.bf=bf
        self.avg=avg
        self.age=age
        self.hs=hs
        self.teamname="INDIA Red"
        
    def display(self):
        print(self.name,self.m,self.runs,self.sr,self.bf,self.avg,self.age)
        
Batsman("virat",200,110,75000,86.5,12000,43.5,31)
display(Batsman)

'''


class Batsman:
    teamname="INDIA Blue" 
    def __init__(self,name,m,hs,runs,sr,bf,avg,age):
        self.name=name
        self.m=m
        self.runs=runs
        self.sr=sr
        self.bf=bf
        self.avg=avg
        self.age=age
        self.hs=hs
        self.teamname="INDIA Red"
        
    def displaydata(self):
        print(self.name,self.m,self.runs,self.sr,self.bf,self.avg,self.age,self.teamname)
        
Batsman("virat",200,110,75000,86.5,12000,43.5,31)
displaydata(Batsman)
Batsman("naveen",200,110,7500,86.9,12000,43.25,31)
displaydata(Batsman)


    
