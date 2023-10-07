class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1 = len(str1) #6
        len2 = len(str2)#3
        
        gcd_len = math.gcd(len1, len2)#3
        
        divisor = str1[:gcd_len]
        
        if str1 == divisor * (len1 // gcd_len) and str2 == divisor * (len2 // gcd_len):
            return divisor
        else:
            return ""