class Solution:
    def reverseWords(self, s: str) -> str:
        text = s.split() #string into list
        string = ""
        text = text[::-1] #reverse
        for i in range(len(text)):
            string+=text[i]
            string+= " "
        return string.strip(" ")
