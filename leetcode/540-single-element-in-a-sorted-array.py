class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while True:
            i = (l + r) // 2
            l_i, r_i = max(i - 1, 0), min(i + 1, len(nums) - 1)
            if l_i != i and nums[i] == nums[l_i]:
                if (i - l) % 2 == 0:
                    r = i - 2
                else:
                    l = i + 1
            elif r_i != i and nums[i] == nums[r_i]:
                if (r - i) % 2 == 0:
                    l = i + 2
                else:
                    r = i - 1
            else:
                return nums[i]
