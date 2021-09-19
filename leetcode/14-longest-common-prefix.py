# first solution - sort of horizontal scanning

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs_set = set(strs)
        prefix = min(strs_set)
        while strs_set:
            temp = strs_set.pop()
            temp_index = 0
            stop = False
            while not stop:
                if len(prefix) > temp_index:
                    if prefix[temp_index] != temp[temp_index]:
                        stop = True
                    else:
                        temp_index += 1
                else:
                    stop = True
            prefix = prefix[:temp_index]
            if len(prefix) == 0:
                return ''
        return prefix       

# found solution - vertical scanning

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = []
		# Create one iterator per string using zip, it will stop at the shortest string
		# s is a tuple of characters at current position for each string
		# create a set to test unicity
        for s in zip(*strs):
            if len(set(s)) != 1:
                break
            result.append(s[0])
        return "".join(result)

# do other solutions - https://leetcode.com/problems/longest-common-prefix/solution/

# divide and conquer and binary search

