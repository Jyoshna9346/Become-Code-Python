##closed path program
'''
def closedPaths(number):
    closedPaths=0
    while number:
        r=number%10
        number//=10
        if r==0:
            closedPaths+=1
        if r==4:
            closedPaths+=1
        if r==6:
            closedPaths+=1
        if r==8:
            closedPaths+=2
        if r==9:
            closedPaths+=1
    return(closedPaths)
'''
#4bit
'''
def fourthbit(number):
    arr[]
    while number>0:
        rem=number%2
        arr.append(rem)
        number=int(number/2)
    return arr[3]
'''
#fizzbuz
def FizzBuzz(n):
    if n%3==0 and n%5==0:
        return "Fizzbuz"
    elif n%3==0:
        return "Fizz"
    elif n%5==0:
        return "Buzz"
    else:
        return str(n)
n=int(input("enter a number"))
print(FizzBuz(n))


