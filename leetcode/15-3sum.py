# first solution

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        r_list = []
        set_nums = set(nums)
        for n in set_nums:
            for m in set_nums:
                if -(n + m) in set_nums:
                    if ((n == m) and nums.count(n) < 2) or ((n == -(n + m)) and nums.count(n) < 2) or \
                        ((-(n + m) == m) and nums.count(-(n + m)) < 2) or ((-(n + m) == n == m) and nums.count(-(n + m)) < 3):
                        continue
                    r_list.append(tuple(sorted((n, m, -(n + m)))))
        return [list(e) for e in set(r_list)]


# second solution

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        d = dict()
        s = set()
        for i, c in enumerate(nums):
            d[c] = d.get(c, []) + [i]
        for i, c1 in enumerate(nums):
            d[c1].remove(i)
            if d[c1] == []:
                del d[c1]
            for c2 in d.keys():
                c3 = -(c1 + c2)
                if c3 in d.keys() and not (c3 == c2 and len(d[c2]) == 1):
                    s.add(tuple(sorted((c1, c2, c3))))
        return [list(x) for x in s]

# third solution

class Solution:
        
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = nums[i]
            right = len(nums) - 1
            left = i + 1
            while left < right:
                if nums[left] + nums[right] + target == 0:
                    l.append([target, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif -(nums[left] + nums[right]) < target:
                    right -= 1
                elif -(nums[left] + nums[right]) > target:
                    left += 1
        return l
                
