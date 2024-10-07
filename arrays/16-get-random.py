import random

class RandomizedSet:
    def __init__(self):
        self.valS = {}  # Dictionary to store value to index mapping
        self.valA = []  # List to store values

    def insert(self, val: int) -> bool:
        if val in self.valS:
            return False
        else:
            self.valA.append(val)
            self.valS[val] = len(self.valA) - 1
            return True

    def remove(self, val: int) -> bool:
        if val not in self.valS:
            return False

        # Get index of the element to remove
        idx_to_remove = self.valS[val]
        
        # Replace the element to remove with the last element in the list
        last_element = self.valA[-1]
        self.valA[idx_to_remove] = last_element
        self.valS[last_element] = idx_to_remove

        # Remove the last element from the list and the dictionary
        self.valA.pop()
        del self.valS[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.valA)

# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
print(obj.insert(-1))
print(obj.remove(-2))
print(obj.insert(-2))
print(obj.getRandom())
print(obj.remove(-1))
print(obj.remove(-2))
# print(obj.getRandom())