def height(self, root):
  if root is None:
      return 0

  return max(self.height(root.left), self.height(root.right)) + 1
