# recursion solve

class Solution:
    def recurse(self, l, i_s):
        if not i_s:
            self.end_l.append(l)
        else:
            for x in i_s:
                self.recurse(l + [self.nums[x]], i_s - {x})
                
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.end_l = []
        l, i_s = [], {x for x in range(len(nums))}
        self.recurse(l, i_s)
        return self.end_l

class Solution:

    def recurse(self, s, r):
        if not s:
            self.l.append(r)
        for x in s:
            self.recurse(s - {x}, r + [x])

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.l = []
        self.recurse(set(nums), [])
        return self.l
