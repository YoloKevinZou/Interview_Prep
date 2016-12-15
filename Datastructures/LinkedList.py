class LinkedListNode:
	def __init__(self, value):
		self.value = value
		self.next = None

	def __str__(self):
		return str(self.value)

class LinkedList:
	def __init__(self):
		self.head = LinkedListNode(-1)
		self.end = self.head

	def append(self, value): 
		newNode = LinkedListNode(value)
		self.end.next = newNode
		self.end = self.end.next

	def search(self, value):
		p = self.head.next
		while p:
			if p.value == value:
				return p
			p = p.next

		return -1

	def delete(self, value):
		prev = self.head
		cur = self.head.next
		while cur: 
			if cur.value == value:
				prev.next = cur.next
				return True
			prev = prev.next
			cur = cur.next

		return False

	def __str__(self):
		result = ""
		p = self.head.next
		while p:
			result += str(p.value) + ","
			p = p.next
		return result


if __name__ == "__main__":
	linkedList = LinkedList()
	linkedList.append(5)
	linkedList.append(2)
	linkedList.append(3)
	linkedList.append(1)

	print(linkedList)
	print(linkedList.search(3))
	print(linkedList.search(4))
	print(linkedList.delete(5))
	print(linkedList)
	print(linkedList.delete(4))
	print(linkedList)
	print(linkedList.delete(1))
	print(linkedList)
	print(linkedList.delete(3))
	print(linkedList)
