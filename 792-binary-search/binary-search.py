class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left=0
        right = len(nums)-1
        found = False
        current = 0
        l=len(nums)
        while left <= right:
            current = left+((right-left)//2)
            if nums[current]==target:
                return current
            elif nums[current]<target:
                left = current+1
            else:
                right = current-1
        return -1
            

