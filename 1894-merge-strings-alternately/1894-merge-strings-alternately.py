class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        min_len = min(len(word1), len(word2))
        
        for i in range(min_len):
            result += word1[i] + word2[i]
        
        result += word1[min_len:] + word2[min_len:]
        
        return result



#         w1_ch = len(word1)
#         w2_ch = len(word2)
#         result =""
#         if w1_ch == w2_ch:
#             for i in range(w1_ch):
#                 result += (word1[i] + word2[i])
#         if w2_ch < w1_ch:
#             for i in range(w2_ch):
#                 result += (word1[i] + word2[i])
#             result+=word1[w2_ch:]
#         if w1_ch < w2_ch:
#             for i in range(w1_ch):
#                 result += (word1[i] + word2[i])
#             result+= word2[w1_ch:]
#         return result