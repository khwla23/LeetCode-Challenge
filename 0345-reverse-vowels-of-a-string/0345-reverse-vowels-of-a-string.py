class Solution:
    def reverseVowels(self, s: str) -> str:
        newA = []
        vowel = 'aeiou'
        st = list(s)
        for i in range(len(s)):
            if st[i].lower() in vowel:
                newA.append(st[i])
        for i in range(len(s)):
            if st[i].lower() in vowel:
                st[i] = newA.pop()

        return ''.join(st)
        

