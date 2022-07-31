# first solution (slow)

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        d = {}
        w_len = len(words[0])
        for w in words:
            h = hash(w)
            d[h] = d.get(h, 0) + 1
        matched = 0
        l = []
        for i in range(len(s) - w_len * len(words) + 1):
            h = hash(s[i:i+w_len])
            if h in d:
                temp_d = d.copy()
                temp_d[h] -= 1
                if temp_d[h] >= 0:
                    matched += 1
            else:
                continue
            temp_i = i
            while matched != len(words):
                temp_i += w_len
                h = hash(s[temp_i:temp_i+w_len])
                if h in temp_d:
                    temp_d[h] -= 1
                    if temp_d[h] >= 0:
                        matched += 1
                    else:
                        break
                else:
                    break
            if matched == len(words):
                l.append(i)
            matched = 0
        return l
