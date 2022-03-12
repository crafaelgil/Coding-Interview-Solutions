def is_same_tree_recursive(p, q): #nodes p, q
  if p is None and q is None:
    return True

  if p is None or q is None or p.val != q.val:
    return False

  return is_same_tree_recursive(p.left, q.left) and is_same_tree_recursive(p.right, q.right)

def is_same_tree_iterative(p,q):
  queue = [p,q]

  while len(queue) != 0:
    first = queue.pop()
    second = queue.pop()

    if first is None and second is None:
      continue

    if first is None or second is None or first.val != second.val:
      return False
    else:
      queue.append(first.left)
      queue.append(second.left)
      queue.append(first.right)
      queue.append(second.right)

  return True
