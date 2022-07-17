# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        while (r - l) > 1:
            index = (r + l) // 2
            if isBadVersion(index) == True:
                r = index
            else:
                l  = index + 1
        return l if isBadVersion(l) else r

# second

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r, lbv = 0, n, n
        while l < r:
            i = (l + r) // 2
            if isBadVersion(i):
                r = lbv = i
            else:
                l = i + 1
        return lbv
        
# more simple and omptimized


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        while l <= r:
            index = (r + l) // 2
            if isBadVersion(index) == False:
                l  = index + 1
            else:
                r = index - 1
        return l
