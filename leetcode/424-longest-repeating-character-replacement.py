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
