class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dic={}
        for i in nums:
            if i not in dic.keys():
                dic[i]=1
            else:
                dic[i]+=1
        c=0
        for i in dic.values():
            c+=i*(i-1)//2
        return c


 Your input
[1,2,3,1,1,3]
Output
4
Expected
4
