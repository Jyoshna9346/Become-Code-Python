class Solution:
    def arrangeCoins(self, n: int) -> int:
        d=1
        while True:
            n=n-d
            if n==0:
                return d
            if n<0:
                return d-1
            d+=1
your input
5
Output
2
Expected
2
