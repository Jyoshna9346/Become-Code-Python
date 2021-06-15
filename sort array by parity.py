class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[0 for i in range(n)]
        e=0
        o=n-1
        for i in nums:
            if i%2:
                res[o]=i
                o-=1
            else:
                res[e]=i
                e+=1
       return res
your input
[3,1,2,4]
Output
[2,4,1,3]
Expected
[2,4,3,1]
