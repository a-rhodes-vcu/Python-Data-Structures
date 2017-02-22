class Binary_Search_Tree:
    """Base Class representing a Binary Search Tree Structure"""
    # Jet fuel can't melt binary trees #

    class _BST_Node:
        """Private class for storing linked nodes with values and references to their siblings"""
        def __init__(self, value):
            """Node Constructor with 3 attributes"""
            self._value = value     # value being added
            self._left = None       # left sibling node (if val less than parent)
            self._right = None      # right sibling node (if val greater than parent)

    def __init__(self):
        """Binary Tree Constructor (creates an empty binary tree)"""
        self._root = None     # Binary tree root
        self._height = 0      # Number of values in the tree

    def get_root(self):
        return self._root

    def insert_element(self, value):
        """Method to insert an element into the BST"""
        if self._root is None:                         # if there is a root in the tree
            self._root = Binary_Search_Tree._BST_Node(value)   # create a new root equal to value
        else:
            self._insert_element(value, self._root)  # insert an element, calls recursive function
        self._height += 1

    def _insert_element(self, value, node):
        """Private method to Insert elements recursively"""
        # if node._value == value:  # if we come across a value already in the list
        #    raise ValueError
        if value < node._value:
            if node._left is not None:  # if a left node child node exists
                return self._insert_element(value, node._left)
                # call the insert element function again to evaluate next node
            else:
                node._left = Binary_Search_Tree._BST_Node(value)
                # after recursively crawling through the tree add value to left leaf
        else:
            if node._right is not None:  # if a right node child node exists
                return self._insert_element(value, node._right)
                # call the insert element function again to evaluate next node
            else:
                node._right = Binary_Search_Tree._BST_Node(value)
                # after recursively crawling through the tree add value to right leaf

    def find(self, value):
        """Return the if value is in tree"""
        current_node = self._root
        while current_node is not None:
            if value == current_node._value:
                return "Found!"
            elif value < current_node._value:
                current_node = current_node._left
            else:
                current_node = current_node._right
        return "Value not Found in Tree!"

    def find_parent(self, value):
        """Non-recursive parent finder, uses a while loop"""
        current_node = self._root
        while current_node._value is not None:
            if current_node._left._value == value or current_node._right._value == value:
                break
            elif value < current_node._value:
                current_node = current_node._left
            else:
                current_node = current_node._right
        return current_node  # test with ._value

    def parent_finder(self, value):
        """Method to find parent, call recursive method: _parent_finder"""
        if self._root is not None:
            return self._parent_finder(value, self._root)
        else:
            raise ValueError('The Binary Tree is Empty')

    def _parent_finder(self, value, node):
        """Private Recursive Method find calls"""
        if node._left._value == value or node._right._value == value:
            return node  # test with ._value
        elif value < node._value and node._left is not None:
            return self._parent_finder(value, node._left)
        else:
            return self._parent_finder(value, node._right)

    def remove_element(self, value):
        # Remove the value specified from the tree. Select the minimum
        # value to the from the right as this element's replacement.
        # Take note of when to move a node reference and when to replace
        if self._root is None:
            raise ValueError('Cannot remove value from an empty tree!')
        else:
            self._remove_element(value, self._root)

    def _remove_element(self, value, node):
        """Private, recursive method that removes a specified value from the binary tree.
        This method calls get_min and _remove_min when the node to be removed has two children"""
        # if node is None:  # may be delete this
        #    return node
        if value < node._value:
            if node._left is not None:
                return self._remove_element(value, node._left)
            else: #
                return node  # raise ValueError('Value not Found!')
        elif value > node._value:
            if node._right is not None:
                return self._remove_element(value, node._right)
            else:
                return node  # raise ValueError('Value not Found!')
        else:  # value == node._value, found it
            self.delete_element(node)

    def delete_element(self, node):
        if node is None:   # may need to change
            return node
        else:
            self._delete_element(node)

    def _delete_element(self, node):
        if node._left is not None and node._right is not None:  # 2 children
            node._value = node._right._value
            if node._right._left is None and node._right._right is None:
                node._right = None
            else:
                return self._delete_element(node._right)
        elif node._left is None and node._right is not None:    # 1 right child
            node._value = node._right._value
            if node._right._left is None and node._right._right is None:
                node._right = None
            else:
                return self._delete_element(node._right)
        elif node._left is not None and node._right is None:   # 1 left child
            node._value = node._left._value
            if node._left._left is None and node._left._right is None:
                node._left = None
            else:
                return self._delete_element(node._left)
        else:  # 0 children # node = None
            if self._height > 1:
                parent = self.parent_finder(node._value)
                if parent._left and parent._left._value == node._value:
                    parent._left = None
                else:
                    parent._right = None
            else:
                self._root = None

    def get_min(self, node):
        """Method is called by remove_element to find the min value in a node's right subtree.
        It is used in the case when you are removing node that has two children.
        Returns Values!"""
        if node._right is not None:  # should never been none, don't really need this!
            if node._right._left is None:
                return node._right._value
            else:
                return self._get_min(node._right)
        else:
            raise ValueError('Parent does not have two children')

    def _get_min(self, node):
        """Private, recursive method called by get_min to find the min value
        in a right subtree (used by remove_element method)"""
        if node._left is None:
            return node._value
        else:
            return self._get_min(node._left)

    def in_order(self):
        # Construct and return a string representing the in-order
        # traversal of the tree. Empty trees should be printed as [ ].
        # Trees with one value should be printed in as [ 4 ]. Trees with
        # more than one value should be printed as [ 4, 7 ]. Note the spacing.
        # Your solution must be recursive. This will involve the introduction
        # of additional private methods to support the recursion control
        # variable.
        pass # TODO replace pass with your implementation

    def pre_order(self):
        # Construct an return a string representing the pre-order
        # traversal of the tree. Empty trees should be printed as [ ].
        # Trees with one value should be printed in as [ 4 ]. Trees with
        # more than one value should be printed as [ 4, 7 ]. Note the spacing.
        # Your solution must be recursive. This will involve the introduction
        # of additional private methods to support the recursion control
        # variable.
        pass # TODO replace pass with your implementation

    def post_order(self):
        # Construct an return a string representing the post-order
        # traversal of the tree. Empty trees should be printed as [ ].
        # Trees with one value should be printed in as [ 4 ]. Trees with
        # more than one value should be printed as [ 4, 7 ]. Note the spacing.
        # Your solution must be recursive. This will involve the introduction
        # of additional private methods to support the recursion control
        # variable.
        pass # TODO replace pass with your implementation

    def get_height(self):
        return self._height
        # return an integer that represents the height of the tree.
        # assume that an empty tree has height 0 and a tree with one
        # node has height 1. This method must operate in constant time.

    def __str__(self):
        return self.in_order()

    def print_tree(self):
        if self._root is not None:
            self._print_tree(self._root)

    def _print_tree(self, node):
        if node is not None:
            self._print_tree(node._left)
            print(str(node._value))
            self._print_tree(node._right)

if __name__ == '__main__':
    bst = Binary_Search_Tree()
    #print(bst.get_height())
    bst.insert_element(12)
    bst.insert_element(7)
    bst.insert_element(3)
    bst.insert_element(20)
    bst.insert_element(9)
    bst.insert_element(25)
    bst.insert_element(16)
    c = bst.find_parent(3)
    b = bst.parent_finder(3)
    print("Parent: " + str(b))
    a = bst.get_root()
    print(" ")
    #print("Min of Right Sub-Tree: " + str(bst.get_min(a)))   # works
    print("-------------------------")
    print(" ")

    print("Binary Tree: ")
    #print(bst.get_height())
    #print(bst.find(2))
    #print(bst.get_height())
    print("Printing Tree: " + str(bst.print_tree()))
    print("-------------------")
    print(" ")

    print("Binary Tree: ")
    bst.remove_element(16)
    print("Printing Tree: " + str(bst.print_tree()))
    print("-------------------")
    print(" ")

