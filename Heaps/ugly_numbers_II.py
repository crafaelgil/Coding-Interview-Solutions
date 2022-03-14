import heapq

def find_nth_ugly_number(n):
  hp = [1]
  top = 1
  for _ in range(n):
      top = hp[0]
      heapq.heappop(hp)
      if not top*2 in hp:
          heapq.heappush(hp,top*2)
      if not top*3 in hp:
          heapq.heappush(hp,top*3)
      if not top*5 in hp:
          heapq.heappush(hp,top*5)
  return top
