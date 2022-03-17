def merge_two_linked_lists(list1, list2):
  curr = newNode()
  prev = curr

  while list1 and list2:
    if list1.val <= list2.val:
      curr.next = list1
      list1 = list1.next
    else:
      curr.next = list2
      list2 = list2.next

    curr = curr.next

  curr = list1 if list1 else list2

  return prev
