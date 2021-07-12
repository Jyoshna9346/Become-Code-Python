
'''
def fun(n):
    if n<=1:
        return n
    return fun(n-1)+fun(n-2)
n=int(input())
print(fun(n)) #fun(n)//5
'''
'''
def fun(n):
    if n<=1:
        return
    print(n)
    fun(n-1)
    fun(n-2)
n=int(input())
fun(n)

input = 5

5
4
3
2
2
3
2

'''
'''
def fun(n):
    if n<=1:
        print('H',n)
        return
    print(n)
    fun(n-1)
    fun(n-2)
    fun(n-3)
n=int(input())
fun(n)

5
5
4
3
2
H 1
H 0
H -1
H 1
H 0
2
H 1
H 0
H -1
H 1
3
2
H 1
H 0
H -1
H 1
H 0
2
H 1
H 0
H -1
'''

'''
def fun(n):
    if n<=1:
        return
    print(n)
    fun(n-1)
    fun(n-2)
n=int(input())
fun(n)

input=6
6
5
4
3
2
2
3
2
4
3
2
2
'''
'''
def fun(n):
    if n<=1:
        return
    print(n)
    fun(n-2)
    fun(n-1)
n=int(input())
fun(n)

input=6
6
4
2
3
2
5
3
2
4
2
3
2
'''
def fun(n):
    if n<=1:
        return
    fun(n-2)
    fun(n-1)
    print(n)
n=int(input())
fun(n)
