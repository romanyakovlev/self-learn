
# recursive

class Solution:
    def recurse(self, nums, p_l, i):
        if len(nums) == i:
            self.l.append(p_l)
            return
        self.recurse(nums, p_l + [nums[i]], i + 1)
        self.recurse(nums, p_l, i + 1)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.l = []
        self.recurse(nums, [], 0)
        return self.l

# iterative

class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        l = [[]]
        for n in nums:
            l += [s + [n] for s in l]
        return l

# bit manipulation

class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        return [
            [nums[bit_i] for bit_i, bit in enumerate(bin(i)[3:]) if bit == '1']
            for i in range(2**n, (2**(n + 1)))
        ]
