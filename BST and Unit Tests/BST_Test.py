import unittest
from Binary_Search_Tree import Binary_Search_Tree


class BST_Tester(unittest.TestCase):
    def setUp(self):
        self._BST = Binary_Search_Tree()

    def test_(self):
        self.assertEqual('[ ]', str(self._BST), 'Empty list should print as "[ ]"')
        self.assertEqual(0, self._BST.get_height())


    def test_remove_leaf_case_1(self):
        self._BST.insert_element(12)
        self._BST.insert_element(7)
        self._BST.insert_element(3)
        self._BST.insert_element(9)
        self._BST.insert_element(20)
        self._BST.insert_element(30)
        self._BST.insert_element(25)
        self._BST.insert_element(16)
        self._BST.remove_element(3)
        self.assertEqual('[ 12, 7, 9, 20, 16, 30, 25 ]', str(self._BST.pre_order()))
        self.assertEqual('[ 9, 7, 16, 25, 30, 20, 12 ]', str(self._BST.post_order()))
        self.assertEqual('[ 7, 9, 12, 16, 20, 25, 30 ]', str(self._BST.in_order()))
        self.assertEqual(4, self._BST.get_height())


    def test_remove_leaf_case_2(self):
        self._BST.insert_element(12)
        self._BST.insert_element(7)
        self._BST.insert_element(3)
        self._BST.insert_element(9)
        self._BST.insert_element(20)
        self._BST.insert_element(16)
        self._BST.insert_element(25)
        self._BST.remove_element(16)
        self.assertEqual('[ 12, 7, 3, 9, 20, 25 ]', str(self._BST.pre_order()))
        self.assertEqual('[ 3, 9, 7, 25, 20, 12 ]', str(self._BST.post_order()))
        self.assertEqual('[ 3, 7, 9, 12, 20, 25 ]', str(self._BST.in_order()))
        self.assertEqual(3, self._BST.get_height())

    def test_remove_case_right(self):
        self._BST.insert_element(12)
        self._BST.insert_element(7)
        self._BST.insert_element(3)
        self._BST.insert_element(9)
        self._BST.insert_element(20)
        self._BST.insert_element(10)
        self._BST.insert_element(16)
        self._BST.insert_element(25)
        self._BST.remove_element(10)
        self.assertEqual('[ 12, 7, 3, 9, 20, 16, 25 ]', str(self._BST.pre_order()))
        self.assertEqual('[ 3, 9, 7, 16, 25, 20, 12 ]', str(self._BST.post_order()))
        self.assertEqual('[ 3, 7, 9, 12, 16, 20, 25 ]', str(self._BST.in_order()))
        self.assertEqual(3, self._BST.get_height())

    def test_remove_left(self):
        self._BST.insert_element(12)
        self._BST.insert_element(7)
        self._BST.insert_element(3)
        self._BST.insert_element(9)
        self._BST.insert_element(8)
        self._BST.insert_element(20)
        self._BST.insert_element(16)
        self._BST.insert_element(25)
        self._BST.remove_element(8)
        self.assertEqual('[ 12, 7, 3, 9, 20, 16, 25 ]', str(self._BST.pre_order()))
        self.assertEqual('[ 3, 9, 7, 16, 25, 20, 12 ]', str(self._BST.post_order()))
        self.assertEqual('[ 3, 7, 9, 12, 16, 20, 25 ]', str(self._BST.in_order()))
        self.assertEqual(3, self._BST.get_height())

    def test_remove_two(self):
        self._BST.insert_element(12)
        self._BST.insert_element(7)
        self._BST.insert_element(3)
        self._BST.insert_element(9)
        self._BST.insert_element(8)
        self._BST.insert_element(20)
        self._BST.insert_element(16)
        self._BST.insert_element(25)
        self._BST.remove_element(20)
        self.assertEqual('[ 12, 7, 3, 9, 8, 25, 16 ]', str(self._BST.pre_order()))
        self.assertEqual('[ 3, 8, 9, 7, 16, 25, 12 ]', str(self._BST.post_order()))
        self.assertEqual('[ 3, 7, 8, 9, 12, 16, 25 ]', str(self._BST.in_order()))
        self.assertEqual(4, self._BST.get_height())



    def test_remove_two_children(self):
        self._BST.insert_element(12)
        self._BST.insert_element(7)
        self._BST.insert_element(3)
        self._BST.insert_element(9)
        self._BST.insert_element(8)
        self._BST.insert_element(20)
        self._BST.insert_element(16)
        self._BST.insert_element(25)
        self._BST.remove_element(7)
        self.assertEqual('[ 12, 8, 3, 9, 20, 16, 25 ]', str(self._BST.pre_order()))
        self.assertEqual('[ 3, 9, 8, 16, 25, 20, 12 ]', str(self._BST.post_order()))
        self.assertEqual('[ 3, 8, 9, 12, 16, 20, 25 ]', str(self._BST.in_order()))
        self.assertEqual(3, self._BST.get_height())

    def test_remove_root(self):
        self._BST.insert_element(12)
        self._BST.insert_element(7)
        self._BST.insert_element(3)
        self._BST.insert_element(9)
        self._BST.insert_element(8)
        self._BST.insert_element(20)
        self._BST.insert_element(16)
        self._BST.insert_element(25)
        self._BST.remove_element(12)
        self.assertEqual('[ 16, 7, 3, 9, 8, 20, 25 ]', str(self._BST.pre_order()))
        self.assertEqual('[ 3, 8, 9, 7, 25, 20, 16 ]', str(self._BST.post_order()))
        self.assertEqual('[ 3, 7, 8, 9, 16, 20, 25 ]', str(self._BST.in_order()))
        self.assertEqual(4, self._BST.get_height())

    def test_remove_root(self):
        self._BST.insert_element(12)
        self._BST.insert_element(7)
        self._BST.insert_element(3)
        self._BST.insert_element(9)
        self._BST.insert_element(8)
        self._BST.insert_element(20)
        self._BST.insert_element(16)
        self._BST.insert_element(25)
        self._BST.remove_element(20)
        self._BST.remove_element(7)
        self.assertEqual('[ 12, 8, 3, 9, 25, 16 ]', str(self._BST.pre_order()))
        self.assertEqual('[ 3, 9, 8, 16, 25, 12 ]', str(self._BST.post_order()))
        self.assertEqual('[ 3, 8, 9, 12, 16, 25 ]', str(self._BST.in_order()))
        self.assertEqual(3, self._BST.get_height())

    def test_remove_root_2(self):
        self._BST.insert_element(12)
        self._BST.remove_element(12)
        self.assertEqual('[ ]', str(self._BST.pre_order()))
        self.assertEqual('[ ]', str(self._BST.post_order()))
        self.assertEqual('[ ]', str(self._BST.in_order()))
        self.assertEqual(0, self._BST.get_height())



if __name__ == '__main__':
    unittest.main()