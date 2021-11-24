# slow naive solution (cause of string concat n-1)

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = 0
        while i < len(digits):
            if (digits[len(digits) - 1 - i] + 1) == 10:
                digits[len(digits) - 1 - i] = 0
                if (len(digits) - 1) == i:
                    return [1] + digits
            else:
                digits[len(digits) - 1 - i] += 1
                break
            i += 1
        return digits
        
