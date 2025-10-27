class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix = 0
        count = 0
        freq = {0: 1}          # prefix sum 0 seen once (empty prefix)

        for x in nums:
            prefix += x
            # number of earlier prefixes with sum = prefix - k
            count += freq.get(prefix - k, 0)
            # record this prefix
            freq[prefix] = freq.get(prefix, 0) + 1

        return count
