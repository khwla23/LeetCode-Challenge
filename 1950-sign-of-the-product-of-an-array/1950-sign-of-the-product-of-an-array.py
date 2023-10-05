class Solution:
    def arraySign(self, nums: List[int]) -> int:

        #Second try to make it more optimize
        prod = 1
        for n in nums:
            if n == 0: # anything multiply by zero is zero
                return 0
            prod *= n

        if prod > 0:
            return 1
        else:
            return -1
'''
        #my First Try
        prod = 1
        for i in nums:
            prod *= i

        if prod < 0:
            return -1
        elif prod > 0:
            return 1
        else:
            return 0
'''

        