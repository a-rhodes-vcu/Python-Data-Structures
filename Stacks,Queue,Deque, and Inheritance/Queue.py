from Deque import Deque

class Queue:

    def __init__(self):
      self._dq = Deque()

    def __str__(self):
      return str(self._dq)

    def __len__(self):
      return len(self._dq)

    def enqueue(self, val):
      self._dq.push_back(val)
      #first in first out

    def dequeue(self):
      x = self._dq.pop_front()
      return x

if __name__ == '__main__':
    pass