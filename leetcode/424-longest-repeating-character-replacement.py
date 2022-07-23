# first solution (slow)

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_counter = 0
        window_counter = 0
        d = {}
        for i in range(len(s)):
            d[s[i]] = d.get(s[i], 0) + 1
            window_counter += 1
            while max(d.items(), key=lambda x:x[1])[1] + k < window_counter:
                index = i - window_counter + 1
                d[s[index]] -= 1
                if d[s[index]] == 0:
                    del d[s[index]]
                window_counter -= 1
            max_counter = max(max_counter, window_counter)
        return max_counter

# second solution (fast)
# this is a tricky one - more clear solution without optimization
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_counter = 0
        win_counter = 0
        d = {}
        win_start = 0
        for i in range(len(s)):
            d[s[i]] = d.get(s[i], 0) + 1
            win_counter += 1
            while d[s[win_start]] + k < win_counter:
                d[s[win_start]] -= 1
                if d[s[win_start]] == 0:
                    del d[s[win_start]]
                win_counter -= 1
                win_start += 1
            k_diff = k - (win_counter - d[s[win_start]])
            win_counter_with_k_diff = min(len(s), win_counter + k_diff)
            max_counter = max(max_counter, win_counter_with_k_diff)
        return max_counter
"""

# the idea is to create sliding window and expand it until full_window = d[s[win_start]] + k reaches 
# the limit (in this case - full_window < win_counter) - that means we cannot get substring greater than this value
# after that - window shrinks from left until full_window = d[s[win_start]] + k is true again.
# repeat until the end of string.
# need to add that d[s[win_start]] + k may be greater than string len because we can have case like this:
# AAAB 2 - 2 here is k and that means are able to change not only B but other chars (AAA)
# to prevent this we need to limit d[s[win_start]] + k as string len

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_counter = 0
        win_counter = 0
        win_start = 0
        d = {}
        for i in range(len(s)):
            d[s[i]] = d.get(s[i], 0) + 1
            win_counter += 1
            full_win = d[s[win_start]] + k
            while full_win < win_counter:
                d[s[win_start]] -= 1
                if d[s[win_start]] == 0:
                    del d[s[win_start]]
                win_counter -= 1
                win_start += 1
                full_win = d[s[win_start]] + k
            max_counter = max(max_counter, full_win)
        return min(len(s), max_counter)
