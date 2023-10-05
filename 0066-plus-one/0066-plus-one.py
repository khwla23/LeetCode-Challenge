class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #More Optimize
        n = len(digits)#4
        carry = 1 
        
        for i in range(n - 1, -1, -1):
            digits[i] += carry
            carry = digits[i] // 10 
            digits[i] %= 10  # Update digits
            
        if carry:
            digits.insert(0, carry)
        
        return digits


"""
        #First TRY
        #case 1 simple
        if digits[-1] != 9:
            digits[-1] += 1
        elif (len(digits) == 1):
            #if there is only 9 => 10
            digits[-1] = 0
            digits.insert(0, 1)
        else:
            #case of 9
            digits[-1] = 0
            digits[-2] += 1

        return digits
"""