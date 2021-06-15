class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        def sums(num):
            s=0
            while num:
                r=num%10
                num=num//10
                s+=r
            return s
        dic={}
        for i in range(lowLimit,highLimit+1):
            s=sums(i)
            if s not in dic.keys():
                dic[s]=1
            else:
                dic[s]+=1
        return max(dic.values())
            
Your input
1
10
Output
2
Expected
2
