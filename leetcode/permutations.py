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
        
