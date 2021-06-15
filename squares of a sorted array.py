


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=len(nums)
        for i in range(n):
            nums[i]=nums[i]*nums[i]
        return sorted(nums)





'''

Your input
[-4,-1,0,3,10]
Output
[0,1,9,16,100]
Expected
[0,1,9,16,100]
'''
