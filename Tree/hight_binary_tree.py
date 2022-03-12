def height_recursive(self, root):
  if root is None:
      return 0

  return max(self.height(root.left), self.height(root.right)) + 1

def height_iteraitve(self, root):
  if root is None:
    return 0

  level = []

  level.append(root)
  height = 0

  while True:
    num_nodes = len(level)
    if num_nodes == 0:
      return height

    height += 1

    while num_nodes > 0:
      node = level[0]
      level.pop(0)

      if node.left is not None:
        level.append(node.left)
      if node.right is not None:
        level.append(node.right)

      num_nodes -= 1
