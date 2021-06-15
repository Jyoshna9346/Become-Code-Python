class Solution:
    def addDigits(self, num: int) -> int:
        res=0
        while num:
            r=num%10
            num=num//10
            res=res+r
            if num==0 and res>9:
                num=res
                res=0
        return res

your input
38
Output
2
Expected
2
