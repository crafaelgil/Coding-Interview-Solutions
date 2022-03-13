def is_symetric(root):
  return is_mirror(root, root)

def is_mirror(root1, root2):
  if root1 is None and root2 is None:
    return True

  if root1 is not None and root2 is not None:
    if root1.val == root2.val:
      return (is_mirror(root1.left, root2.right) and is_mirror(root1.right, root2.left))

  return False
