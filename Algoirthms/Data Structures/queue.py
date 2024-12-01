class Queue_array():
    def __init__(self, size):
        self.size = size 
        self.__queue = [None] * size
        self.__write = 0
        self.__read = 0
    
    def enqueue(self, key):
        # insert from the back, one position before write pointer
        
        self.__queue[self.__write] = key
        if self.__write == self.size - 1:
            self.__write = 0
        else:
            if (self.__write + 1) != self.__read:
                self.__write += 1
            else:
                print("index error: write and read cannot be at the same index")

    def dequeue(self):
        # pop from the front, where the read pointer is at
        self.__queue[self.__read] = None
        if self.__read == self.size - 1:
            self.__read = 0
        else:
            self.__read += 1

    def empty(self):
        if self.__write == self.__read:
            return True
        return False


queue = Queue_array(5)

queue.enqueue(3)
queue.enqueue(4)

a = queue.dequeue()

print(a)
