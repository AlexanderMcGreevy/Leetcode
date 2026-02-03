class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        for x in nums:
            if x not in dict:
                dict[x]=1
            dict[x]+=1
        return max(dict, key=dict.get)
        