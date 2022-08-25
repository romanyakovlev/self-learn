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
                
# resolve

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = - nums[i]
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == target:
                    result.append([nums[i], nums[l], nums[r]])
                    while l < len(nums) - 1 and nums[l] == nums[l + 1]:
                        l += 1
                    while r > 0 and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        return result

# solution with explanation

def threeSum(self, nums):
    nums.sort()
    result = []
    for left in range(len(nums) - 2): # renamed this to left because this will always be the leftmost pointer in the triplet
        if left > 0 and nums[left] == nums[left - 1]: # this step makes sure that we do not have any duplicates in our result output
            continue 
        mid = left + 1 # renamed this to mid because this is the pointer that is between the left and right pointers
        right = len(nums) - 1
        while mid < right:
            curr_sum = nums[left] + nums[mid] + nums[right]
            if curr_sum < 0:
                mid += 1 
            elif curr_sum > 0:
                right -= 1
            else:
                result.append([nums[left], nums[mid], nums[right]])
                while mid < right and nums[mid] == nums[mid + 1]: # Another conditional for not calculating duplicates
                    mid += 1
                while mid < right and nums[right] == nums[right - 1]: # Avoiding duplicates check
                    right -= 1
                mid += 1
                right -= 1
    return result
