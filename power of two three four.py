class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        p=0
        while 3**p<n:
            p=p+1
        return 3**p==n

 Your input
27
Output
true
Expected
true


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        p=0
        while 4**p<n:
            p=p+1
        return 4**p==n
 Your input
16
Output
true
Expected
true

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        p=0
        while 2**p<n:
            p=p+1
        return 2**p==n
your input 1
Output
true
Expected
true
