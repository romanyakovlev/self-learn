# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 0, n
        while l <= r:
            target = (l + r) // 2
            if guess(target) == 0:
                return target
            elif guess(target) == -1:
                r = target - 1
            elif guess(target) == 1:
                l = target + 1  
