class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res=0
        for num in nums:
            if (len(str(num))%2==0):
                res+=1
        return res

    
your input [12,345,2,6,7896]
Output
2
Expected
2
