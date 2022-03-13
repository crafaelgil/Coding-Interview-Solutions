def height(self,root, ans):
    if (root == None):
        return 0

    left_height = self.height(root.left, ans)
    right_height = self.height(root.right, ans)

    ans[0] = max(ans[0], 1 + left_height + right_height)

    return 1 + max(left_height, right_height)

# Computes the diameter of binary
# tree with given root.
def diameter(self,root):
    if (root == None):
        return 0
    ans = [-999999999999]
    height_of_tree = self.height(root, ans)
    return ans[0]
