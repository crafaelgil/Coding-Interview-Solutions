import heapq as hp

def find_k_closest_points(points, k):
  points.sort(key=lambda point: point[0]**2 + point[1]**2)

  return points[:k]

def find_k_closest_points_min_heap_solution(points, k):
  min_heap = []

  for x, y in points:
      dist = x**2 + y**2
      min_heap.append([dist, x, y])

  hp.heapify(min_heap)

  k_closest_points = []

  for i in range(k):
      dist, x, y = hp.heappop(min_heap)
      k_closest_points.append([x,y])

  return k_closest_points
