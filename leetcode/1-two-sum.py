# first solution

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for x_i, x in enumerate(nums):
            if x not in d.keys():
                d[x] = [x_i]
            else:
                d[x].append(x_i)
        for x in d.keys():
            x_i = d[x].pop()
            y = target - x
            if y in d.keys() and len(d[y]):
                y_i = d[y].pop()
                return [x_i, y_i]

# second solution

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i, n in enumerate(nums):
            v = target - n
            if v in d.keys():
                return [d[v], i]
            else:
                d[n] = i
        

# better solution

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for x_i, x in enumerate(nums):
            y = target - x
            if y not in d.keys():
                d[x] = x_i
            else:
                return x_i, d[y]
            
# good article about sums from leetcode (2sum, 3/4 sum, etc)
# https://leetcode.com/problems/two-sum/discuss/737092/Sum-MegaPost-Python3-Solution-with-a-detailed-explanation
