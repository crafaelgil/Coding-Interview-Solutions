class Node:
  def __init__(self, data = None, left = None, right = None):
    self.data = data
    self.left = left
    self.right = right

def check_for_bst(root: Node):
  stack = []
  prev = None

  while root or stack:
    while root:
      stack.append(root)
      root = root.left
    root = stack.pop()
    if prev and root.data <= prev.data:
      return False
    prev = root
    root = root.right
  return True

if __name__ == '__main__':
  root = Node(1)
  root.left = Node(2)
  root.right = Node(3)
  root.left.right = Node(4)
  root.right.left = Node(5)
  root.right.right = Node(6)
  root.right.left.left = Node(7)
  root.right.left.right = Node(8)

  print(check_for_bst(root))
