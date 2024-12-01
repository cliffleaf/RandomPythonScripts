class LinearHashTable:
    def __init__(self, size=7):
        self.__size = size
        self.__slots = [None for i in range(size)]
    
    def __str__(self):
        return str(self.__slots)
    
    def get_hash_index(self, key):
        return key % self.__size
    
    def __len__(self):
        count = 0
        for item in self.__slots:
            if item:
                count += 1
        
        return count
    
    def put(self, key):
        index = self.get_hash_index(key)
        if self.__slots[index] is None:
            self.__slots[index] = key
        
        else:
            temp = key
            while self.__slots[index] is not None:
                temp += 1
                index = self.get_hash_index(temp)
            self.__slots[index] = key
    
    def __getitem__(self, index):
        return self.__slots[index]
    
    def search(self, key):
        '''
        THIS IS A LINEAR HASHING
        '''
        ori_index = self.get_hash_index(key)
            
        step = 1
        temp = key
        index = ori_index
        
        while not self.__slots[index] == key:
            if step == self.__size:
                return False, step
            if self.__slots[index] is None:
                return False, step
                
            temp += 1
            index = self.get_hash_index(temp)
            step += 1
            
        return True, step  