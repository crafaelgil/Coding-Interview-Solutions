from ast import keyword
from pickle import TRUE
import queue
import symbol
from turtle import st

from numpy import append


class Solution:
  def __init__(self):
    self.st = st

  def check_parenthesis(self, st):
    open_parenthesis = tuple('({[')
    close_parentehsis = tuple(')}]')
    map = dict(zip(open_parenthesis, close_parentehsis))

    queue = []

    for ch in st:
      if ch in open_parenthesis:
        queue.append(map[ch])
      elif ch in close_parentehsis:
        if not queue or ch != queue.pop():
          return False

    if not queue:
      return True
    else:
      return False

st = "[()]{}{[()()]()}"
solution = Solution()

print(solution.check_parenthesis(st))
