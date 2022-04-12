from collections import deque
class HitCounter(object):
  def __init__(self):
    self.num_secs = 300
    self.dq = deque() #[timestamp, num_hits]
    self.num_hits = 0

  def register_hit(self, timestamp):
    self.get_num_hits(timestamp)
    if self.dq and self.dq[-1][1] == timestamp:
      self.dq[-1][1] += 1
    else:
      self.dq.append([timestamp, 1])

    self.num_hits += 1

  def get_num_hits(self, timestamp):
    while self.dq and self.dq[0][0] <= timestamp - self.num_secs:
      self.num_hits -= self.dq.popleft()[1]
    return self.num_hits

counter = HitCounter()
counter.register_hit(1)
counter.register_hit(2)
counter.register_hit(3)
print(counter.get_num_hits(4))
counter.register_hit(300)
print(counter.get_num_hits(300))
print(counter.get_num_hits(301))

