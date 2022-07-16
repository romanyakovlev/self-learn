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

