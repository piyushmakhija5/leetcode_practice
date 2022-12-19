## https://leetcode.com/problems/insert-delete-getrandom-o1/description/

class RandomizedSet:

    def __init__(self):
        self.set = []

    def insert(self, val: int) -> bool:
        if val not in self.set:
            self.set.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.set:
            self.set.pop(self.set.index(val))
            return True
        else:
            return False

    def getRandom(self) -> int:
        return self.set[random.randint(0, len(self.set)-1)]



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
