class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sep_i = None
        for i in range(len(nums)):
            if nums[i] >= 0 and sep_i is None:
                sep_i = i
            nums[i] = nums[i] ** 2
        if sep_i is None:
            sep_i = len(nums) - 1
        if sep_i is not None and sep_i != 0:
            l = []
            neg_i, pos_i = sep_i - 1, sep_i
            while neg_i >= 0 and pos_i <= (len(nums) - 1):
                if nums[neg_i] <= nums[pos_i]:
                    l.append(nums[neg_i])
                    neg_i -= 1
                else:
                    l.append(nums[pos_i])
                    pos_i += 1
            if neg_i >= 0:
                l += nums[neg_i::-1]
            if pos_i <= (len(nums) - 1):
                l += nums[pos_i:]
            return l
        else:
            return nums

# two pointers solution

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        result = [None for _ in A]
        left, right = 0, len(A) - 1
        for index in range(len(A)-1, -1, -1):
            if abs(A[left]) > abs(A[right]):
                result[index] = A[left] ** 2
                left += 1
            else:
                result[index] = A[right] ** 2
                right -= 1
        return result
