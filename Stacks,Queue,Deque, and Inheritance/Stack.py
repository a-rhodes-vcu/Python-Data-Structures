from Deque import Deque

class Stack:

    def __init__(self):
      self._dq = Deque()

    def __str__(self):
      return str(self._dq)

    def __len__(self):
      return len(self._dq)

    def push(self, val):
      self._dq.push_front(val)

    def pop(self):
      x = self._dq.pop_front()
      return x

    def peek(self):
      x = self._dq.peek_front()
      return x

if __name__ == '__main__':
    pass