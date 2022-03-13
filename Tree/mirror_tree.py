def mirror_tree_recursive(root):
  if root is None:
    return

  mirror_tree_recursive(root.left)
  mirror_tree_recursive(root.right)

  root.left, root.right = root.right, root.left
