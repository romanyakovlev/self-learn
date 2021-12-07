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
