# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def height(root):
            if root is None:
                return 0, True

            lh, lb = height(root.left)
            rh, rb = height(root.right)

            if abs(lh - rh) <= 1 and lb and rb:
                return 1 + max(lh, rh), True
            return 0, False
        x,bal=height(root)
        return bal


        