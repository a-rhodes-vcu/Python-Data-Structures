from Linked_List import Linked_List

class Deque:
    def __init__(self):
        self._list = Linked_List()

    def __str__(self):
        return str(self._list)

    def __len__(self):
        return len(self._list)

    def push_front(self, val):
        new = Linked_List._Node(val)
        if len(self._list)==0:
            self._list.append_element(val)
        else:
            self._list.insert_element_at(val,0)
        #working

    def pop_front(self):
        x  = self._list.remove_element_at(0)
        return x
        # working

    def peek_front(self):
        x = self._list.get_element_at(0)
        return x
        #working

    def push_back(self, val):
        self._list.append_element(val)
        #working

    def pop_back(self):
        x = self._list.remove_element_at(len(self._list)-1)
        return x
        #working

    def peek_back(self):
        x = self._list.get_element_at (len(self._list)-1)
        return x
        #working

if __name__ == '__main__':
    d = Deque()
    print(d)
    #pass  # Unit tests make this unnecessary



