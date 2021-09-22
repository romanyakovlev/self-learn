# first algo

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        for i in range(len(haystack)):
            if i + len(needle) <= len(haystack) and haystack[i] == needle[0] \
                    and haystack[i + len(needle) - 1] == needle[-1]:
                l_index, r_index = 0, len(needle) - 1
                while True:
                    if haystack[i + l_index] == needle[l_index] \
                            and haystack[i + r_index] == needle[r_index]:
                        if l_index >= r_index:
                            return i
                        l_index += 1
                        r_index -= 1
                    else:
                        break
        return -1

        
# to do: KMP, Rabin Karp
