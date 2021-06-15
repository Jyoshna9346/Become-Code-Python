class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        i=1
        res=start
        start=2+start
        while(i<n):
            res=res^start
            start=2+start
            i=i+1
        return res


your input
5
0
Output
8
Expected
8
