class Solution:
    def average(self, salary: List[int]) -> float:
        mini = min(salary)
        maxi = max(salary)
        # finding sum
        total_sum = sum(salary)
        # sum = 0
        # for item in salary:
        #         sum += item
            
        return (total_sum - mini - maxi) / (len(salary) - 2)
