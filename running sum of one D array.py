class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n=len(nums)
        for i in range(1,n):
            nums[i]=nums[i]+nums[i-1]
        return nums



your input [1,2,3,4]
Output
[1,3,6,10]
Expected
[1,3,6,10]
