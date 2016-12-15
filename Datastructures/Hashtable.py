from LinkedList import *

class Hashtable:
	def __init__(self, size):
		self.array = [ LinkedList() for _ in range(size)]
		self.size = size

	def getIndex(self, key):
		return hash(key) % self.size

	def insert(self, key, value):
		index = self.getIndex(key)
		linkedList = self.array[index]
		node = linkedList.searchWithKey(key)
		if node:
			node.value = value
		else:
			linkedList.appendWithKey(key,value)

	def search(self, key):
		index = self.getIndex(key)
		linkedList = self.array[index]
		return linkedList.searchWithKey(key)

	def delete(self, key):
		index = self.getIndex(key)
		linkedList = self.array[index]
		return linkedList.deleteWithKey(key)

	def __str__(self):
		result = ""
		for i in self.array:
			result += str(i) + "\n"

		return result

if __name__ == "__main__":	
	hashTable = Hashtable(10)
	hashTable.insert("a", 3)
	hashTable.insert(2, 2)
	hashTable.insert(5, 5)
	hashTable.insert(3, 6)
	hashTable.insert(1, 3)
	hashTable.insert(5, 0)
	hashTable.insert("a", 5)
	print(hashTable)
	hashTable.delete(5)
	hashTable.delete("a")
	hashTable.delete("b")
	print(hashTable)
	hashTable.insert(2, 4)
	print(hashTable)	






