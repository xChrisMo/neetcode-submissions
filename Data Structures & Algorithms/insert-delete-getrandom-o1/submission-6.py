import random

class RandomizedSet:

    def __init__(self):
        # keep a dict
        # keep a list
        self.store = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        # adds into set, 
        # if NOT in, return True
        # else, False

        # on insert, add to dict..
        # the lenghty of the arr would be the value
        # if not in arr, append, use that as value eitherways
        give_bool = val in self.store

        # would this be overwritten if it is already in ? 'Inserts an item val into the set if not present.'
        if not give_bool:
            self.arr.append(val)
            self.store[val] = len(self.arr) - 1

        return not give_bool

    def remove(self, val: int) -> bool:
        # removes from set
        # if was in, True
        # else, False
        # retrive from dict, to get array position
        # swap array position with end of list
        # update in dict
        # remove last element from array
        # return bool
        give_bool = val in self.store

        if give_bool:
            # finding last value and its index
            last_val = self.arr[-1]

            # index of val for removal in arr
            index_to_delete = self.store[val]

            # move last element there
            self.arr[index_to_delete] = last_val

            # replace position of lastval in dict to be the index we need delete
            self.store[last_val] = index_to_delete

            del self.store[val]
            self.arr.pop()  # removes last index


        return give_bool

    def getRandom(self) -> int:
        # returns random from the set. 
        # return random from arr
        return random.choice(self.arr)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()