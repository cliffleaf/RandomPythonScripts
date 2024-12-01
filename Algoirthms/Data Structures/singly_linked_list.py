'''
Advantage of linked list: 
    when adding or removing a value, the other elements don't need to be shifted (unlike array)
    because all we need to do is to change two pointers. 
    Imagine a bunch of arrows (pointers pointing to nodes), hence more efficient to add or remove from middle

    __iter__ function is an iterator for linked list, create another LinkedListIterator class to implement this

'''

class ListNode():
    '''
    printing a ListNode will only return a map object since it is a class
    '''
    def __init__(self, val):
        self.val = val
        self.next = None

# without a tail
class singly_linked_list():

    def __init__(self, size = 0):
        '''
        self.head is a ListNode object, not a value
        it is like a head pointer, which is always None, and not counted into index
        Therefore, size = 0 even when head is present
        '''
        self.size = size
        self.head = None

    def print_list(self) -> None:
        node = self.head
        print("Printing the list elements: ", end = "")

        while node is not None:
            print(node.val, end=" ")
            node = node.next
        print()

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.size:
            return -1
        
        curr_node = self.head
        for _ in range(index + 1):
            curr_node = curr_node.next
        return curr_node.val
        

    def push_front(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list.
        """
        self.insert_at(0, val)
        

    def push_back(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.size += 1
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = ListNode(val)
        

    def insert_at(self, index: int, val: int) -> None:
        """
        Add node before the index-th node in the linked list.
        """
        if index < 0 or index > self.size:
            return
        self.size += 1  # because we are adding a node
        
        predecessor = self.head
        
        for _ in range(index):
            # print(predecessor.val, end = " ")
            predecessor = predecessor.next
        
        # new_node points to the node that is originally at this index
        # predecessor (at index - 1) points to new_node
        # first pred.next refers to the node, while the second pred.next refers to the pointer
        new_node = ListNode(val)
        new_node.next = predecessor.next 
        predecessor.next = new_node
        

    def pop_at(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.size:
            return
        self.size -= 1
        predecessor = self.head
        
        for _ in range(index):
            predecessor = predecessor.next
        predecessor.next = predecessor.next.next


list1 = singly_linked_list()
