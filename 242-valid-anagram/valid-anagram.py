class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
            
        temp = t
        for x in s:
            if x in temp:
                temp=temp.replace(x,"",1)
            else:
                return False
        if len(temp) == 0:
            return True
        return False
        