class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        d=(nums[-1]-1)*(nums[-2]-1)
        return d
    
Your input
[3,4,5,2]
Output
12
Expected
12
