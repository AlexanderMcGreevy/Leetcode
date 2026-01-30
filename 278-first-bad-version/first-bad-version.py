# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        lb=1
        rb=n
        while lb < rb:
            m= (rb-lb)//2 + lb
            if isBadVersion(m):
                rb= m
            else:
                lb = m +1
        return lb
            
        
            
        