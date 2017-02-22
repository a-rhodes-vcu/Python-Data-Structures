import unittest
from Deque import Deque
from Stack import Stack
from Queue import Queue


class DSQTester(unittest.TestCase):
    def setUp(self):
        self._deque = Deque()
        self._stack = Stack()
        self._queue = Queue()

    def test_empty_list_string(self):
        self.assertEqual('[ ]', str(self._deque), 'Empty list should print as "[ ]"')

    def test_add_head_empty(self):
        self._deque.push_front('Victory')
        self.assertEqual('[ Victory ]', str(self._deque))

    def test_add_tail_empty(self):
        self._deque.push_back('Victory')
        self.assertEqual('[ Victory ]', str(self._deque))

    def test_add_head_with_one(self):
        self._deque.push_front('Data')
        self._deque.push_front('Structures')
        self.assertEqual('[ Structures, Data ]', str(self._deque))

    def test_remove_head_with_one(self):
        self._deque.push_front('Data')
        self._deque.push_front('Structures')
        self._deque.pop_front()
        self.assertEqual('[ Data ]', str(self._deque))

    def test_add_tail_with_two(self):
        self._deque.push_back('Data')
        self._deque.push_back('Structures')
        self.assertEqual('[ Data, Structures ]', str(self._deque))

    def test_add_front_with_two(self):
        self._deque.push_back('Data')
        self._deque.push_back('Structures')
        self._deque.push_back('Rocks')
        self._deque.pop_back()
        self.assertEqual('[ Data, Structures ]', str(self._deque))

    def test_add_back_with_two(self):
        self._deque.push_back('Rocks')
        self._deque.push_back('Structures')
        self._deque.push_back('Data')
        self.assertEqual('[ Rocks, Structures, Data ]', str(self._deque))

    def test_add_four_front(self):
        self._deque.push_front('Data')
        self._deque.push_front('and')
        self._deque.push_front('Algorithms')
        self._deque.push_front('Structures')
        self._deque.peek_front()
        self.assertEqual('[ Structures, Algorithms, and, Data ]', str(self._deque))

    def test_add_four_back(self):
        self._deque.push_back('Structures')
        self._deque.push_back('Algorithms')
        self._deque.push_back('Data')
        self._deque.push_back('and')
        self._deque.peek_back()
        self.assertEqual('[ Structures, Algorithms, Data, and ]', str(self._deque))





if __name__ == '__main__':
    unittest.main()