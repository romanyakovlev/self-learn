# first solution

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d_p, d = {}, {}
        win_count = 0
        for c in s1:
            d_p[c] = d_p.get(c, 0) + 1
        for i in range(len(s2)):
            d[s2[i]] = d.get(s2[i], 0) + 1
            win_count += 1
            if win_count == len(s1):
                if d == d_p:
                    return True
                left_win_index = i - win_count + 1
                d[s2[left_win_index]] -= 1
                if d[s2[left_win_index]] == 0:
                    del d[s2[left_win_index]]
                win_count -= 1
        return False

# second solution

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d_s1, d_s2 = {}, {}
        for c in s1:
            d_s1[c] = d_s1.get(c, 0) + 1
        win_start = 0
        for win_end in range(len(s2)):
            d_s2[s2[win_end]] = d_s2.get(s2[win_end], 0) + 1
            if (win_end - win_start + 1) == len(s1):
                if d_s2 == d_s1:
                    return True
                d_s2[s2[win_start]] -= 1
                if d_s2[s2[win_start]] == 0:
                    del d_s2[s2[win_start]]
                win_start += 1
        return False
