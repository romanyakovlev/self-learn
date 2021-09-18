# basic string reverse

class Solution:
    def reverse(self, x: int) -> int:
        neg = True if x < 0 else False
        str_x = ('-' if neg else '') + str(x).lstrip('-')[::-1]
        result = int(str_x)
        if -2**31 > result or result > (2**31 - 1):
            return 0
        return result

# mod

class Solution:
    def reverse(self, x: int) -> int:
        neg = -1 if x < 0 else 1
        x = abs(x)
        result = '0'
        while x > 0:
            digit = x % 10
            x //= 10
            result += str(digit)
        result = neg * int(result)
        return 0 if -2**31 > result or result > (2**31 - 1) else return result

# favorite solution from discuss

class Solution(object):
    def reverse(self, x):
        result = 0
        symbol = 1
        
        if x < 0:
            symbol = -1
            x = -x

        while x:
            result = result * 10 + x % 10
            x /= 10
            
        return 0 if result > pow(2,31) else result * symbol
