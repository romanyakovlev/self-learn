class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        has_word = False
        c = 0
        for i in range(len(s)):
            if s[len(s) - 1 - i] != ' ':
                has_word = True
            if s[len(s) - 1 - i] == ' ' and not has_word:
                c += 1
            elif s[len(s) - 1 - i] == ' ' and has_word:
                return i - c
        return len(s) - c

# second solution (from desc)

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        i, length = len(s) - 1, 0
        
        while s[i] == ' ':
            i -= 1
        
        while s[i] != ' ' and i >= 0:
            i -= 1
            length += 1
        return length


# python-way

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])
