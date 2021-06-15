class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        dic={}
        for i in nums:
            if i not in dic.keys():
                dic[i]=1
            else:
                dic[i]+=1
        s=0
        for k,v in dic.items():
            if v==1:
                s+=k
        return s

    
Your input
[1,2,3,2]
Output
4
Expected
4



    
