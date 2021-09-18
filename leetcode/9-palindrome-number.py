# algo with string converting

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        k = 0
        x = str(x)
        middle = len(x) // 2
        while (k + 1) <= middle:
            if x[k] == x[-(k+1)]:
                k += 1
                continue
            else:
                return False
        else:
            return True

# same but short

class Solution:
    def isPalindrome(self, x: int) -> bool:
    	if x < 0:
    		return False
    	
    	return str(x) == str(x)[::-1]

# algo without string convert

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        temp_x = x
        result = 0
        while temp_x > 0:
            digit = temp_x % 10 
            result = result * 10 + digit
            temp_x //= 10
        return True if result == x else False
