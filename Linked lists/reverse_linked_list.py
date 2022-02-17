class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class Linked_List:
  def print_linked_list_elements(self, head: Node):
    while head.next is not None:
      print(head.data, end="->")
      head = head.next
    print(head.data)

  def find_mid_element(self, head: Node):
    if head is None:
      return -1

    if head.next is None:
      return head.data

    output = head

    while head:
      if head.next is None:
        break
      head = head.next.next
      output = output.next

    return output.data

  def reverse_linked_list(self, head: Node):
    if head is None or head.next is None:
      return head

    prev = None
    current = head

    while current is not None:
      next = current.next
      current.next = prev
      prev = current
      current = next

    self.print_linked_list_elements(prev)

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

linked_list = Linked_List()

linked_list.print_linked_list_elements(node1)
print("*****")
linked_list.reverse_linked_list(node1)

