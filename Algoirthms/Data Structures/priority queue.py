class PriorityQueue:
    def __init__(self):
        self.__binary_heap = [0]
        self.__size = 0
    
    def __len__(self):
        return self.__size
    
    def __str__(self):
        return str(self.__binary_heap)
    
    def add_all_ignore_order(self, a_list):
        for item in a_list:
            self.__binary_heap.append(item)
            self.__size += 1
    
    def percolate_up(self, index):
        while self.__binary_heap[index] < self.__binary_heap[index // 2]:
            
            self.__binary_heap[index], self.__binary_heap[index//2] = self.__binary_heap[index//2], self.__binary_heap[index]
            index = index // 2
    
    def insert(self, num):
        self.__binary_heap.append(num)
        self.__size += 1
        self.percolate_up(self.__size)
    
    def get_smaller_child_index(self, index):
        if index * 2 + 1 <= len(self.__binary_heap) - 1:
            if self.__binary_heap[index * 2] <= self.__binary_heap[index * 2 + 1]:
                return index * 2
            else:
                return index * 2 + 1
        else:
            return index * 2
    
    def percolate_down(self, index):
        if index * 2 > self.__size:
            return
        else:
            toSwap = self.get_smaller_child_index(index)
            if self.__binary_heap[index] > self.__binary_heap[toSwap]:
                self.__binary_heap[index], self.__binary_heap[toSwap] = self.__binary_heap[toSwap], self.__binary_heap[index]
                self.percolate_down(toSwap)
    
    def get_minimum(self):
        if self.__size == 0:
            return
        return self.__binary_heap[1]
    
    def delete_minimum(self):
        new_root = self.__binary_heap.pop(len(self.__binary_heap)-1)
        old_minimum = self.get_minimum()
        self.__binary_heap[1] = new_root
        
        self.percolate_down(1)
        
        return old_minimum