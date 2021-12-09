# classic pythonic-way solution (faster than other solutions because of c-extention python modules)

class Solution:
    
    def reverseWords(self, s: str) -> str:
        return ' '.join([w[::-1] for w in s.split()])

# first ugly solution

class Solution:
    
    def reverseWord(self, s, l, r):
        while l <= r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
    
    def reverseWords(self, s: str) -> str:
        s = list(s)
        l, r = 0, len(s) - 1
        start, end = 0, 0
        while end < len(s) - 1:
            if s[end] == ' ' and end > start:
                self.reverseWord(s, start, end - 1)
                start = end + 1
            end += 1
        if end > start:
            self.reverseWord(s, start, end)
        return ''.join(s)

# solition using recursion

class Solution:
    
    def reverseWord(self, s, l=None, r=None):
        if l is None:
            l = 0
        if r is None:
            r = len(s) - 1
        if l == r:
            return s[l]
        elif r - l == 1:
            return s[r] + s[l]
        else:
            return s[r] + self.reverseWord(s, l+1, r-1) + s[l]
    
    def recurseSentence(self, s, start=0, word_before=False):
        if start > len(s):
            return ''
        end = start
        while end < len(s):
            if s[end] == ' ':
                break
            end += 1    
        space = ' ' if word_before else ''
        return (
            space + self.reverseWord(s, start, end - 1) + 
            self.recurseSentence(s, end + 1, word_before=True)
        )
        
    
    def reverseWords(self, s: str) -> str:
        return self.recurseSentence(s)

# two pointer solution

def reverseWords_manual(s):
    res = ''
    l, r = 0, 0
    while r < len(s):
        if s[r] != ' ':
            r += 1
        elif s[r] == ' ':
            res += s[l:r + 1][::-1]
            r += 1
            l = r
    res += ' '
    res += s[l:r + 2][::-1]
    return res[1:]
            

# word reversed by recursion
# recurse('abc') -> 'cba'

def recurse(s, l=None, r=None):
    if l is None:
        l = 0
    if r is None:
        r = len(s) - 1
    if l == r:
        return s[l]
    elif r - l == 1:
        return s[r] + s[l]
    else:
        return s[r] + recurse(s, l+1, r-1) + s[l]
