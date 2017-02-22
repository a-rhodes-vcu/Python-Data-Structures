class Binary_Search_Tree:
  # TODO.I have provided the public method skeletons. You will need
  # to add private methods to support the recursive algorithms
  # discussed in class

  class _BST_Node:
    # TODO The Node class is private. You may add any attributes and
    # methods you need.

    def __init__(self, value):
        """Node Constructor with 3 attributes"""
        self._value = value  # value being added
        self._left = None  # left sibling node (if val less than parent)
        self._right = None  # right sibling node (if val greater than parent)
        self._size = 0

  def __init__(self):
    self._root = None
    self._size = 0
    self._height = 0

  def insert_element(self, value):
      """Method to insert an element into the BST"""
      if self._root is None:  # if there is a root in the tree
          self._root = Binary_Search_Tree._BST_Node(value)  # create a new root equal to value
      else:
          self._insert_element(value, self._root)  # insert an element, calls recursive function
      self._size = self._size + 1

  def _insert_element(self, value, node):
    if value < node._value:
        if node._left is not None:  # if a left node child node exists
            return self._insert_element(value, node._left)
              # call the insert element function again to evaluate next node
        else:
            node._left = Binary_Search_Tree._BST_Node(value)
              # after recursively crawling through the tree add value to left leaf
    else:
        if node._right is not None:
            return self._insert_element(value, node._right)
              # call the insert element function again to evaluate next node
        else:
            node._right = Binary_Search_Tree._BST_Node(value)
              # after recursively crawling through the tree add value to right leaf

  def lookup(self):
      self._lookup(self._root)

  def _lookup(self, node):
      while node._left is not None:
          node = node._left
      return node

  def remove_element(self, value):
    if self._root is None:
        print("There is nothing to remove")
    self._remove_element(value, self._root)

  def _remove_element(self, value, node):
      # key is value
      # node is root

        if node is None:
            return node

        elif value < node._value:
          node._left =  self._remove_element(value, node._left)

        elif value > node._value:
          node._right =  self._remove_element(value, node._right)
        else:
            if node._left is None and node._right is None:
              del node
              node = None
              return node
            elif node._left is None:
                temp = node
                node = node._right
                del temp
            elif node._right is None:
                temp = node
                node = node._left
                del temp
            elif node._left is None:
                temp = node
                node = node._right
                del temp
            else:
                temp = self._lookup(node._right)
                node._value = temp._value
                node._right = self._remove_element(temp._value, node._right)
        return node

  def get_left(self, value):
      self._get_left(value, self._root)
  def get_right(self, value):
      self._get_right(value, self._root)

  def _get_left(self, value, node):
      if node is None or value is None:
          print("Not found")
      elif node._value < value:
          x = value
          print(x)
          parent = node._value
          print(parent)
          return self._get(value, node._right)
  def _get_right(self, value, node):
      if node is None or value is None:
          print("Not found")
      elif node._value > value:
          x = value
          print(x)
          parent = node._value
          print(parent)
          return self._get(value, node._left)

  def get_height(self):
     print ("the height is: ")
     print(self._get_height(self._root))

  def _get_height(self, node):
      if node is None:
          return 0
      else:
          return max(self._get_height(node._left), self._get_height(node._right)) + 1

  def in_order(self):
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
          return_string = return_string + str(node._value) + ", "
      return return_string


if __name__ == '__main__':
  BST = Binary_Search_Tree()
