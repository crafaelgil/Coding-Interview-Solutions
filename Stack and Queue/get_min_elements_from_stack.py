class Stack:
  def __init__(self):
      self.s = []
      self.minEle=None

  def push(self,x):
      if len(self.s) == 0:
          self.minEle = x
          self.s.append(x)
      else:
          if x < self.minEle:
              self.s.append(2*x - self.minEle)
              self.minEle = x
          else:
              self.s.append(x)

  def pop(self):
      if len(self.s) > 0:
          val = self.s.pop()
          if val >= self.minEle:
              return val
          else:
              tmp = self.minEle
              self.minEle = 2*self.minEle - val
              return tmp
      else:
          return -1

  def find_min_element(self):
      if len(self.s) == 0:
          return -1
      return self.minEle


stack = Stack()

stack.push(1)
stack.push(3)
stack.push(-1)
stack.push(9)
stack.push(-9)
stack.push(4)

print(stack.s)

stack.pop()

print(stack.s)

print(stack.find_min_element())

stack.pop()
stack.pop()

print(stack.s)

print(stack.find_min_element())

