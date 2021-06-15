class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        n=len(salary)
        d=sum(salary[1:-1])
        d=d/(n-2)
        return d


Your input
[4000,3000,1000,2000]
Output
2500.00000
Expected
2500.00000
