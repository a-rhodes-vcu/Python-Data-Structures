#################################################################
# Team Name: TheRevenant
# Binary Search Tree Class
# Project IV: Less Left, More Right
# CSCI 241: Data Structures and Algorithms
#################################################################
class Binary_Search_Tree:
    """Base Class representing a Binary Search Tree Structure"""

    class _BST_Node:
        """Private class for storing linked nodes with values and references to their siblings"""
        def __init__(self, value):
            """Node Constructor with 3 attributes"""
            self._value = value     # value being added
            self._left = None       # left sibling node (if val less than parent)
            self._right = None      # right sibling node (if val greater than parent)
            self._height = 0

    def __init__(self):
        """Binary Tree Constructor (creates an empty binary tree)"""
        self._root = None     # Binary tree root

    def insert_element(self, value):
        """Method to insert an element into the BST"""
        self._root = self._insert_element(value, self._root)  # insert an element, calls recursive function

    def _insert_element(self, value, node):
        """Private method to Insert elements recursively"""
        # if node._value == value:  # if we come across a value already in the list
        #    raise ValueError
        if node is None:
            return Binary_Search_Tree._BST_Node(value)
        if value < node._value:
             node._left = self._insert_element(value, node._left)
        elif value > node._value:  # if a right node child node exists
            node._right = self._insert_element(value, node._right)
        node._height = self.height(node)
        return self.balance(node)

    def remove_element(self, value):
        """Method to remove elements from Binary Tree, calls recursive method: _remove_element"""
        self._root = self._remove_element(value, self._root)

    def _remove_element(self, value, node):
        """Private, recursive method that removes a specified value from the binary tree.
        This method calls get_min and _remove_min when the node to be removed has two children"""
        if node is None:
            return node
        if value < node._value:
            node._left = self._remove_element(value, node._left)
        elif value > node._value:
            node._right = self._remove_element(value, node._right)
        elif node._left is not None and node._right is not None: # 2 kids
            temp = self.get_min(node._right)
            node._value = temp._value
            node._right = self._remove_element(temp._value, node._right)
        elif node._left is None:  # One right child
            node = node._right
                #del temp
        else:                     # One left child
            node = node._left
        #node._height = self.height(node)
        return self.balance(node)

    def balance(self, node):
        allowed_balance = 1
        if node is None:
            return node
        if self.height(node._left) - self.height(node._right) > allowed_balance:
            if self.height(node._left._left) >= self.height(node._left._right):
                node = self._rotate_with_left_child(node)
            else:
                node = self._double_with_left_child(node)
        else:
            if self.height(node._right) - self.height(node._left) > allowed_balance:
                if self.height(node._right._right) >= self.height(node._right._left):
                    node = self._rotate_with_right_child(node)
                else:
                    node = self._double_with_right_child(node)
        node._height = self.height(node)
        return node

    def _rotate_with_left_child(self, k2):
        k1 = k2._left
        k2._left = k1._right
        k1._right = k2
        k2._height = self.height(k2)
        k1._height = self.height(k1)
        return k1

    def _rotate_with_right_child(self, k1):
        k2 = k1._right
        k1._right = k2._left
        k2._left = k1
        k1._height = self.height(k1)
        k2._height = self.height(k2)
        return k2

    def _double_with_left_child(self, k3):
        k3._left = self._rotate_with_right_child(k3._left)
        return self._rotate_with_left_child(k3)

    def _double_with_right_child(self, k1):
        k1._right = self._rotate_with_left_child(k1._right)
        return self._rotate_with_right_child(k1)

    def get_min(self, node):
        while node._left is not None:
            node = node._left
        return node

    def in_order(self):
        """Returns Binary Search Tree as a String in in-order, call recursive _in_order method"""
        if self._root is None:
            return '[ ]'
        else:
            return "[ " + self._in_order(self._root)[:-2] + " ]"

    def _in_order(self, node):
        return_string = ""
        if node is not None:
            return_string = self._in_order(node._left)
            return_string = return_string + str(node._value) + ", "
            return_string = return_string + self._in_order(node._right)
        return return_string

    def pre_order(self):
        """Returns Binary Search Tree as a String in pre-order, call recursive _pre_order method"""
        if self._root is None:
            return '[ ]'
        else:
            return "[ " + self._pre_order(self._root)[:-2] + " ]"

    def _pre_order(self, node):
        return_string = ""
        if node is not None:
            return_string = str(node._value) + ", "
            return_string = return_string + self._pre_order(node._left)
            return_string = return_string + self._pre_order(node._right)
        return return_string

    def post_order(self):
        """Returns Binary Search Tree as a String in post-order, call recursive _post_order method"""
        if self._root is None:
            return '[ ]'
        else:
            return "[ " + self._post_order(self._root)[:-2] + " ]"

    def _post_order(self, node):
        return_string = ""
        if node is not None:
            return_string = self._post_order(node._left)
            return_string = return_string + self._post_order(node._right)
            return_string = return_string + str(node._value) + ", "
        return return_string

    def height(self, node):
        if node is None:
            return 0
        else:
            left_depth = self.height(node._left)
            right_depth = self.height(node._right)
            if left_depth > right_depth:
                return left_depth + 1
            else:
                return right_depth + 1

    def get_height(self):
        return self._get_height(self._root)

    def _get_height(self, node):
        if node is None:
            return 0
        else:
            left_depth = self._get_height(node._left)
            right_depth = self._get_height(node._right)
            if left_depth > right_depth:
                return left_depth + 1
            else:
                return right_depth + 1

    def __str__(self):
        return self.in_order()

if __name__ == '__main__':
    # See Unit Test: BST_Test.py
    # pass
    avl = Binary_Search_Tree()
    #print("Height of Tree; " + str(avl.height(avl)))




    a = avl.get_root()
    print("Height of Tree: " + str(avl.height(a)))
    print("Printing Tree (Pre-Order): " + str(avl.pre_order()))
    print("Printing Tree (Post-Order): " + str(avl.post_order()))
    print("-------------------")
    print("Printing Tree (In-Order): " + str(avl.in_order()))
    print("-------------------")
