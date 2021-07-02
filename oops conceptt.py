#opps concept
'''
def fun():
    print("hai") #no o/p is print here
'''
'''
def fun():
    print('hai')
fun() #here we have to call fun then its print output

ouput:hai
'''
'''
>>> a=10
>>> type(a)
<class 'int'>
>>> a=10.2
>>> type(a)
<class 'float'>
>>> a=''
>>> type(a)
<class 'str'>
>>> pow(2,3)
8
'''
'''
append(10)
pop(10)
append.pop(10)
math.sqrt(23)
'''
'''
class ClassName:
    pass #no ouput
'''

#struct student
'''
{
    introllno
    char name[100]:
}
struct student std1,std2; #obj of struct student

*structure:combination of members variables
*class:collection of members variables and member function
'''
'''
class student:
    def__init__(self,rollno,name,branch,per,bc): #structure to write program
        self.rollno=rollno
        self.name=name
        self.branch=branch
        self.per=per
        self.bc=bc
'''
'''
class student:
    def __init__(self):
        print('hi') #ouput is nothing
'''
'''
class student
def __init__(self):
    print('hi')
def fun(self):
    print("fummethod") #ouput is nothing
'''
#object=instance of class(instance=reference)
#class student:
    #def __init__(self):--->init is constructor
       # print('hi')
    #def fun(self):
        #print('funmethod')
    #std1=student()-->object creation
#suppose:
    #std2=student()
'''
class student:
    def __init__(self,rollno,nmae,branch,per,bc):
        self.rollno=rollno
        self.name=name
        self.branch=branch
        self.per=per
        self.bc=bc
std1=student('123','jyoshna','ece','7.9',0)
print(std1,rollno,std1.name)

here ouput is nothing
but when we use print in the program then ouput is 123 jyoshna
'''
types of variable:
    local var
    instance var
    class/static var
