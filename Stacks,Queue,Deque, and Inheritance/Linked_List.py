#################################################################
# Team Name: Bourbon
# Doubly Linked List Class
# Project II: Literally Loving Linked Lists
# CSCI 241: Data Structures and Algorithms
#################################################################

class Linked_List:
    """Base Class containing linked list methods"""
    class _Node:
        """Private class for storing doubly linked nodes with header and trailer"""
        __slots__ = '_val', '_next', '_prev'    # streamlines memory storage

        def __init__(self, val):
            """Node Constructor"""
            self._val = val     # value being added
            self._next = None   # reference to next node
            self._prev = None   # reference to prev node

    def __init__(self):
        """Linked List Constructor"""
        self._header = self._Node(None)         # header set to None
        self._trailer = self._Node(None)        # trailer set to None
        self._header._next = self._trailer      # trailer is after header
        self._trailer._prev = self._header      # header starts the list
        self._size = 0                          # number of values in list

    def append_element(self, val):
        """Adds an element or value to the last position of the Linked List"""
        new = Linked_List._Node(val)
        last_value = self._trailer._prev
        new._next = self._trailer
        self._trailer._prev = new
        new._prev = last_value
        last_value._next = new
        self._size = self._size + 1

    def insert_element_at(self, val, index):
        """Inserts an element or value at a specified index. First Value is indexed as the 1st position."""
        # First value in the list is 0. This is computer science!
        # If the index is not a valid position within the list,
        # raise an IndexError exception. This method cannot
        # be used to add an item at the tail position.
        new = Linked_List._Node(val)
        if index < 0:
            raise IndexError
        if self._size > 0:
            current = self._header
            for i in range(0, index):
                current = current._next
            above_current = current._next
            new._next = above_current
            above_current._prev = new
            new._prev = current
            current._next = new
            self._size += 1

    def remove_element_at(self, index):
        """Removes an element at a specified index. First value is indexed as the 1st position."""
        # If the index is invalid, raise an IndexError exception.
        if index < 0 or index >= self._size:
            raise IndexError
        if self._size == 0:
            raise ValueError('Cannot remove value, list is already empty')
        to_return = self.get_element_at(index)
        current = self._header
        connect_ahead = current._next._next
        for i in range(0, index):
            current = current._next
            connect_ahead = connect_ahead._next
        current._next = current._next._next
        connect_ahead._prev = connect_ahead._prev._prev
        self._size = self._size - 1
        return to_return

    def get_element_at(self, index):
        """Gets an element or value at a specified index, first value in list = 1"""
        # the value stored in the node at the specified
        # index, but do not unlink it from the list. If the
        # specified index is invalid, raise an IndexError exception.
        if index < 0 or index >= self._size:
            raise IndexError
        if self._size == 0:
            raise ValueError
        current = self._header._next
        for i in range(0,index):
            current = current._next
        return current._val

    def __str__(self):
        """Returns a string of representation of the List"""
        # An empty list should appear as [ ].
        # A list with one element should appear as [ 5 ].
        # A list with two elements should appear as [ 5, 7 ].
        # You may assume that the values stored inside of the
        # node objects implement the __str__() method, so you
        # call str(val_object) on them to get their string
        # representations.
        if self._size == 0:
            return '[ ]'
        return_string = "[ "
        for index in range(0, self._size):
            return_string = return_string + str(self.get_element_at(index)) + ", "
        return return_string[:-2] + " ]"
        # -2, used to remove the comma and space in the resulting string

    def __len__(self):
        """Returns the number of value-containing nodes in this list."""
        return self._size

    def __iter__(self):
        """Creating an iter-index-counter for the for-loop"""
        # initialize a new attribute for walking through your list
        self._iter_index = 0
        return self

    def __next__(self):
        """This is used to grab the next value in the list and increments the iter-index-counter"""
        # using the attribute that you initialized in __iter__(),
        # fetch the next value and return it. If there are no more
        # values to fetch, raise a StopIteration exception.
        if self._iter_index == self._size:
            raise StopIteration
        current_val = self.get_element_at(self._iter_index)
        self._iter_index = self._iter_index + 1
        return current_val

if __name__ == '__main__':
    # Your test code should go here. Be sure to look at cases
    # when the list is empty, when it has one element, and when
    # it has several elements. Do the indexed methods raise exceptions
    # when given invalid indices? Do they position items
    # correctly when given valid indices? Does the string
    # representation of your list conform to the specified format?
    # Does removing an element function correctly regardless of that
    # element's location? Does a for loop iterate through your list
    # from head to tail?
    print(" ")   # used to make output easier to read

    ll = Linked_List()
"""
    # Testing conditions on the empty Linked List
    print("_____________________________________")
    print("Testing Certain methods on empty List")
    print("-------------------------------------")
    try:
        print(ll)                   # should return [ ]
        ll.insert_element_at(4, 1)  # should fail, the list is empty
        ll.remove_element_at(1)     # should fail, the list is empty
        ll.get_element_at(1)        # should fail, the list is empty
    except IndexError:
        print("Error(s) Caught: Please enter a valid index.")
    print(" ")
    print(" ")

    # Testing the Append Method (val)
    print("____________________________________")
    print("Testing the 'append_element' method:")
    print("------------------------------------")
    try:
        ll.append_element(0)                    # should append
        a = ll.remove_element_at(1)             # should remove value at 0-th position, just happens to be zero
        print("Element removed = " + str(a))    # should return: 0
        ll.append_element(1)                    # should append
        ll.insert_element_at(0, 1)              # should add zero at the 0-th position (first position)
        ll.append_element(2)                    # should append
    except IndexError:
        print("Error(s) Caught: Please enter a valid index.")
    print("Linked List after appending elements" + str(ll))  # should return: [ 0, 1, 2 ]
    print("Size of the Linked List: " + str(len(ll)))        # should return: 3
    print(" ")
    print(" ")

    # Testing the Insert Method (val, index)
    print("_______________________________________")
    print("Testing the 'insert_element_at' method:")
    print("---------------------------------------")
    try:
        ll.insert_element_at(4, 2)
        ll.insert_element_at(8, 5)    # should fail, out of index
        ll.insert_element_at(30, -1)  # should fail, out of index
    except IndexError:
        print("Error(s) Caught: Please enter a valid index.")
    print("Linked List after inserting elements" + str(ll))  # should return: [ 0, 4, 1, 2 ]
    print("Size of the Linked List: " + str(len(ll)))        # should return: 4
    print(" ")
    print(" ")

    # Testing the Remove Method (index)
    print("_______________________________________")
    print("Testing the 'remove_element_at' method:")
    print("---------------------------------------")
    try:
        b = ll.remove_element_at(2)
        print("Value Removed = " + str(b))
        ll.remove_element_at(0)   # should fail, out of index
        ll.remove_element_at(5)   # should fail, out of index
        ll.remove_element_at(-1)  # should fail, out of index
    except IndexError:
        print("Error(s) Caught: Please enter a valid index.")
    print("Linked List after removing elements: " + str(ll))  # should return: [ 0, 1, 2 ]
    print("Size of the Linked List: " + str(len(ll)))         # should return: 3
    print(" ")
    print(" ")

    # Testing for-loop iteration
    print("___________________________")
    print("Testing for-loop iteration: ")
    print("---------------------------")
    for val in ll:
        print(val)
        # should return:
        # 0
        # 1
        # 2
    print("")
    print("")

    # Testing get element_at Method:
    print("________________________________")
    print("Testing 'get_element_at' Method: ")
    print("--------------------------------")
    try:
        print("Getting Value in the First Position: " + str(ll.get_element_at(1)))
        print("Getting Value in the Second Position: " + str(ll.get_element_at(2)))
        print("Getting Value at Invalid Position (0): " + str(ll.get_element_at(0)))
    except IndexError:
        print("Error(s) Caught: Please enter a valid index.")
"""
