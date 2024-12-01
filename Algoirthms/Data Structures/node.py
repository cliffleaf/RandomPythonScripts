class Node:
    def __init__(self, data, next = None):
        self.__data = data
        self.__next = next
    
    def set_data(self, data):
        self.__data = data
    def set_next(self, next):
        self.__next = next
    
    def get_data(self):
        return self.__data
    def get_next(self):
        return self.__next
    
    def __str__(self):
        return str(self.__data)
    
    def add_after(self, value):
        val_node = Node(value)
        val_node.set_next(self.__next)
        self.set_next(val_node)
    
    def remove_after(self):
        # val.next = val.next.next
        # val.next.next = None
        
        val_next = self.get_next()
        if val_next is None:
            pass
        else:
            self.set_next(val_next.get_next())
            val_next.set_next(None)
    
    def get_count(self):
        curr = self
        count = 0
        while curr is not None:
            count += 1
            curr = curr.get_next()
        return count
    
    def get_words(self):
        curr = self
        word = ""
        
        while curr:
            word += curr.get_data()
            curr = curr.get_next()
            
        return word