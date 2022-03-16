def calculate(self, s: str) -> int:
  result = 0
  num = 0
  sign = 1

  stack = [sign]

  for i in range(len(s)):
      if '0' <= s[i] <= '9':
          num = num * 10 + int(s[i])
      elif s[i] == '+' or s[i] == '-':
          result += sign * num
          sign = stack[-1] if s[i] == '+' else -stack[-1]
          num = 0
      elif s[i] == '(':
          stack.append(sign)
      elif s[i] == ')':
          stack.pop()

  result += sign * num

  return result
