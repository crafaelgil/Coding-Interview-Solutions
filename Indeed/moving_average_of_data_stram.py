import collections

class AverageDataStram:
  def __init__(self, size):
    self.queue = collections.deque()
    self.size = size

  def next(self, val):
    if len(self.queue) == self.size:
      self.queue.popleft()

    self.queue.append(val)

    return sum(self.queue) / len(self.queue)

avg_data_stream = AverageDataStram(3)
print(avg_data_stream.next(1))
print(avg_data_stream.next(10))
print(avg_data_stream.next(3))
print(avg_data_stream.next(5))

