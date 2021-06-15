class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans=[]
        ans.append(0)
        for i in range(0,len(gain)):
            temp=ans[i]+gain[i]
            ans.append(temp)
        return max(ans)

    
Your input
[-5,1,5,0,-7]
Output
1
Expected
1
