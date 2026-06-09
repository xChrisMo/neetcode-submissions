import random
class RandomizedSet:
    def __init__(self):
        #have an array. where its length is value in dict
        self.dictionary = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        flag = val not in self.dictionary

        if flag:
            self.arr.append(val)
            self.dictionary[val] = len(self.arr) - 1

        return flag
        #flag = val not in dict: if val: return 
        #add to arr, 
        #get len array, it is the value in dict, 
        #return bool

    def remove(self, val: int) -> bool:
        #flag = val in dict:
        #if flag,
        #val_index = dictionary[val]
        #get last_ele in arr
        #index of val in arr gets overwrriten by val
        #arr.pop
        #update val of last_ele in dict,
        #del val in dict
        flag = val in self.dictionary

        if flag:
            last_ele = self.arr[-1]
            val_index = self.dictionary[val]
            self.arr[val_index] = last_ele

            self.dictionary[last_ele] = val_index

            del self.dictionary[val]
            self.arr.pop()

        return flag


    def getRandom(self) -> int:
        #return random.choice(self.arr)r
        return random.choice(self.arr)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()