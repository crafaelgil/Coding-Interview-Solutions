from collections import deque

from numpy import size

class Node:
  def __init__(self, data = None, left = None, right = None):
    self.data = data
    self.left = left
    self.right = right

def left_view_iterative(root: Node):
  if root is None:
    return

  queue = deque()
  queue.append(root)

  while queue:
    size = len(queue)
    i = 0
    while i < size:
      child = queue.popleft()
      i+=1
      if i == 1:
        print(child.data, end=" ")
      if child.left:
        queue.append(child.left)
      if child.right:
        queue.append(child.right)

def left_view_recursive(root: Node, level: int, d: dict):
  if root is None:
    return

  if level not in d:
    d[level] = root.data

  left_view_recursive(root.left, level+1, d)
  left_view_recursive(root.right, level+1, d)

def print_left_view(root: Node):
  d = {}

  left_view_recursive(root, 1, d)

  for i in range(1, len(d)+1):
    print(d[i], end=' ')
  print('\n')


if __name__ == '__main__':
  root = Node(1)
  root.left = Node(2)
  root.right = Node(3)
  root.left.right = Node(4)
  root.right.left = Node(5)
  root.right.right = Node(6)
  root.right.left.left = Node(7)
  root.right.left.right = Node(8)

  left_view_iterative(root)
  print('\n')
  print_left_view(root)
