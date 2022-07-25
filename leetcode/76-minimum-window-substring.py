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
        
