# first solution

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d = {}
        for c in t:
            d[c] = d.get(c, 0) + 1
        matched = 0
        min_win, min_str = float("inf"), ""
        win_start = 0
        for win_end in range(len(s)):
            if s[win_end] in d:
                d[s[win_end]] -= 1
                if d[s[win_end]] == 0:
                    matched += 1
            if matched != len(d):
                continue
            while win_start < len(s):
                if s[win_start] in d and d[s[win_start]] < 0:
                    d[s[win_start]] += 1
                    win_start += 1
                elif s[win_start] not in d:
                    win_start += 1
                else:
                    break
            win = win_end - win_start
            if win < min_win:
                min_win, min_str = win, s[win_start:win_end + 1]
            while matched == len(d):
                d[s[win_start]] += 1
                if d[s[win_start]] > 0:
                    matched -= 1
                win_start += 1
        return min_str
        
# second solution (educative)

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d = {}
        for c in t:
            d[c] = d.get(c, 0) + 1
        matched = 0
        win_start = 0
        min_str = s + s[0]
        # try to extend the range [window_start, window_end]
        for win_end in range(len(s)):
            right_char = s[win_end]
            if right_char in d:
                d[right_char] -= 1
                if d[right_char] >= 0: # Count every matching of a character
                    matched += 1
            # Shrink the window if we can, finish as soon as we remove a matched character
            while matched == len(t):
                if len(min_str) > win_end - win_start:
                    min_str = s[win_start:win_end + 1]
                left_char = s[win_start]
                win_start += 1
                if left_char in d:
                    # Note that we could have redundant matching characters, therefore we'll decrement the
                    # matched count only when a useful occurrence of a matched character is going out of the window
                    if d[left_char] == 0:
                        matched -= 1
                    d[left_char] += 1
        if len(min_str) > len(s):
            return ""
        return min_str
