from turtle import st


class Solution:
  def __init__(self, st):
    self.st = st

  def convert_to_int(self):
    values = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    int_value = 0

    for i in range(len(st)):
      if i+2< len(st):
        if st[i:i+2] == 'IV':
          int_value+=4
          i+=2
        if st[i:i+2] == 'IX':
          int_value+=9
          i+=2


    return int_value

st = "IV"
solution = Solution(st)

print(solution.convert_to_int())
