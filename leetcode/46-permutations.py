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
        self.n_limit = len(nums)
        self.end_l = []
        i_s = {x for x in range(len(nums))}
        for x in i_s:
            self.recurse([self.nums[x]], i_s - {x})
        return self.end_l

