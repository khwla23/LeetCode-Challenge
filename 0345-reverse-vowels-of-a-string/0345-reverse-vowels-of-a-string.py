class Solution:
    def reverseVowels(self, s: str) -> str:
        newA = []
        vowel = 'aeiou'
        s = list(s)
        for i in range(len(s)):
            if s[i].lower() in vowel:
                newA.append(s[i])
        for i in range(len(s)):
            if s[i].lower() in vowel:
                s[i] = newA.pop()

        return ''.join(s)
        

