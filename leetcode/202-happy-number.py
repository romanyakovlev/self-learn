class Solution:
    def isHappy(self, n: int) -> bool:
        slow = fast = n
        while True:
            slow = sum([int(x) ** 2 for x in str(slow)])
            fast = sum([int(x) ** 2 for x in str(fast)])
            fast = sum([int(x) ** 2 for x in str(fast)])
            if fast == 1:
                return True
            elif slow == fast:
                return False
