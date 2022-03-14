import collections
import heapq

def reorganize_string(s):
  dic = collections.Counter(s)

  heap = []

  for key in dic:
      heapq.heappush(heap, [-dic[key], key])

  ans = ""
  prev_count, prev_char = None, None

  while heap:
      current_count, current_char = heapq.heappop(heap)

      ans += current_char
      current_count += 1

      if prev_count and prev_count < 0:
          heapq.heappush(heap, [prev_count, prev_char])

      prev_count, prev_char = current_count, current_char

  if len(ans) != len(s):
      return ""
  else:
      return ans
