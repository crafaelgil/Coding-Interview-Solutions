def find_k_closest_points(points, k):
  points.sort(key=lambda point: point[0]**2 + point[1]**2)

  return points[:k]
