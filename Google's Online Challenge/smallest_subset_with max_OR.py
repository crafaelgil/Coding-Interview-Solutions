# 1001 -> 1001
# 1011 -> 1011
# 1101 -> 1111
# OR is increassing
# a | b <= a | b | c because the number of 1s in the result can only increase

def find_set(arr):
  if not arr or len(arr) == 0:
    return []


