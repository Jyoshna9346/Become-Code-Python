class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        n=len(startTime)
        c=0
        for i in range(n):
            if queryTime>=startTime[i] and queryTime<=endTime[i]:
                c+=1
        return c

your input
[1,2,3]
[3,2,7]
4
Output
1
Expected
1
