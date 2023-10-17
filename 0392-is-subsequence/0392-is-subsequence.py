class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        if len(s) == 0:
            return True
        index = 0
        for i in range(len(t)):
            if index <= (len(s) - 1):
                if s[index] == t[i]:
                    index +=1

        if index == len(s):
            return True
        else:
            return False