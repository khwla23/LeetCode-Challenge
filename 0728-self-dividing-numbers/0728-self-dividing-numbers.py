class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for num in range(left, right+1):
            flag = True
            for digit in str(num):
                if digit != '0':
                    if (num % int(digit)) != 0:
                        flag = False
                        break
                else:
                    flag = False
                    break
            if flag:
                result.append(num)
        return result
                

            