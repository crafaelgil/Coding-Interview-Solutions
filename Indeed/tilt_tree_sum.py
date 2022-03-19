# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        sum = [0]
        self.solve(root, sum)
        return sum[0]

    def solve(self, root, sum):
        if root is None:
            return 0
        left = self.solve(root.left, sum)
        right = self.solve(root.right, sum)
        sum[0] += abs(left - right)
        return root.val + left + right
