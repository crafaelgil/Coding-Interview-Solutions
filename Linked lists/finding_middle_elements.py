class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class Linked_List:
  def print_linked_list_elements(self, head: Node):
    while head.next is not None:
      print(head.data)
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

print(linked_list.find_mid_element(node1))


