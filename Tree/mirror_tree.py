def mirror_tree_recursive(root):
  if root is None:
    return

  mirror_tree_recursive(root.left)
  mirror_tree_recursive(root.right)

  root.left, root.right = root.right, root.left

def mirror_tree_iterative(root):
  if root is None:
    return

  level = []

  while len(level) > 0:
    node = level.pop()

    if node is None:
      continue

    node.left, node.right = node.right, node.left

    level.append(node.left)
    level.append(node.right)
