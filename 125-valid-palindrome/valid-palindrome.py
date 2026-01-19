class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        simp=s.lower().strip()
        left=0
        right=len(simp)-1
        while left <= right:
            while left <= right and not simp[left].isalnum():
                left += 1
            while left <= right and not simp[right].isalnum():
                right -= 1
            if left>right:
                break
            if simp[left] != simp[right]:
                return False
            left+=1
            right-=1

        return True
        