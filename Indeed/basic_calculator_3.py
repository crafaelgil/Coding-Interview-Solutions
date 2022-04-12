# def basic_calculator_3(s):
#   def calc(starting_index):
#     i, num, operation, stack = starting_index, 0, '+', []

#     def update_stack(operation, num):
#       if operation == '+':
#         stack.append(num)
#       elif operation == '-':
#         stack.append(-num)
#       elif operation == '*':
#         stack.append(stack.pop() * num)
#       elif operation == '/':
#         stack.append(int(stack.pop() / num))

#     while i < len(s):
#       if '0' <= s[i] <= '9':
#         num = num * 10 + int(s[i])
#       elif s[i] in '+-*/':
#         update_stack(operation, num)
#         operation, num = s[i], 0
#       elif s[i] == '(':
#         num, j = basic_calculator_3(s[i+1:])
#         i += j+1
#       elif s[i] == ')':
#         update_stack(operation, num)
#         return sum(stack), i
#       i+=1

#     update_stack(operation, num)

#     return sum(stack)

#   return calc(0)

def basic_calculator_3(s, staring_index):
  i, num, operation, stack = staring_index, 0, '+', []

  def update_stack(operation, num):
    if operation == '+':
      stack.append(num)
    elif operation == '-':
      stack.append(-num)
    elif operation == '*':
      stack.append(stack.pop() * num)
    elif operation == '/':
      stack.append(int(stack.pop() / num))

  while i < len(s):
    if '0' <= s[i] <= '9':
      num = num * 10 + int(s[i])
    elif s[i] in '+-*/':
      update_stack(operation, num)
      operation, num = s[i], 0
    elif s[i] == '(':
      num, j = basic_calculator_3(s, i+1)
      i += j+1
    elif s[i] == ')':
      update_stack(operation, num)
      return sum(stack), i
    i+=1

  update_stack(operation, num)

  return sum(stack)

s = "(1+2*3) - (-2*3+8)*(-5+(4-2*5))" #= 7-2*(-5+(-6)) = 7-2*(-11) = 29
print(basic_calculator_3(s, 0))
