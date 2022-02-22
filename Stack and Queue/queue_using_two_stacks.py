from inspect import stack


class Solution:
  def __init__(self):
    self.stack1 = []
    self.stack2 = []

  def push(self, x):
    #Move elements from stack1 to stack2
    while len(self.stack1) != 0:
      self.stack2.append(self.stack1[-1])
      self.stack1.pop()

    #append new elements
    self.stack1.append(x)

    #Move back elements to stack1
    while len(self.stack2) != 0:
      self.stack1.append(self.stack2[-1])
      self.stack2.pop()

  def pop(self):
    if not self.stack1:
      return

    ret = self.stack1[-1]
    self.stack1.pop()
    return ret

  def print_queue(self):
    for ele in self.stack1:
      print(ele, end=" ")
    print("\n")
    return

solution = Solution()

solution.push(1)
solution.print_queue()
solution.push(2)
solution.print_queue()
solution.push(3)
solution.print_queue()
solution.push(4)
solution.print_queue()
solution.pop()
solution.print_queue()



