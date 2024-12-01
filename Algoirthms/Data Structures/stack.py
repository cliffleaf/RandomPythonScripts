'''
Stack is a virtual data structure, also know as a LIFO queue
The retrieving of elements follows the rule of Last in, First out
All operations have constant time complexity of O(1)

Can be implemented using array or linked list

Real life applications: matching the parentheses 
'''

class Stack_array():
    def __init__(self, space):
        if not isinstance(space, int):
            print("Space must be an integer")
            return
        self.space = space 
        self.__stack = []  # implement using array, not accessible externally
    
    def size(self):
        return self.space

    def push(self, key):
        try:
            if len(self.__stack) == self.space:
                raise IndexError()    
        except IndexError:
            print("Stack maximum capicity reached")
        else:
            self.__stack.insert(0, key)
    
    def pop(self):
        self.__stack.pop(0)
    
    def top(self):
        return self.__stack[0]
    
    def empty(self):
        if len(self.__stack) == 0:
            return True
        return False
    
    def print_stack(self):
        for element in self.__stack:
            print(element, end=" ")


stack1 = Stack_array(4)
stack1.push(4)
stack1.push(3)
stack1.push(2)
stack1.push(1)


stack1.print_stack()