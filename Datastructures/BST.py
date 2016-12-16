class TreeNode:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

	def __str__(self):
		return str(self.value)

class BST:
	def __init__(self):
		self.root = None

	def insert(self, value):
		if not self.root:
			self.root = TreeNode(value)
		else:
			self.insertHelper(value, self.root)

	def insertHelper(self, value, root):
		if not root:
			return TreeNode(value)
		if value < root.value:
			root.left = self.insertHelper(value, root.left)
		elif value > root.value:
			root.right = self.insertHelper(value, root.right)
		return root

	def search(self, root, value):
		if not root:
			return None

		if root.value == value:
			return root

		if value < root.value:
			return self.search(root.left, value)
		if value > root.value:
			return self.search(root.right, value)

	def findRightMin(self, root):

		if not root:
			return None

		if not root.left:
			return root

		return self.findRightMin(root.left)


	def delete(self, root, value):
		if not root:
			return []

		if value < root.value:
			root.left = self.delete(root.left, value)
		elif value > root.value:
			root.right = self.delete(root.right, value)
		else:
			if not root.left and not root.right:
				root = None
			elif root.left and not root.right:
				root = root.left
			elif not root.left and root.right:
				root = root.right
			else:
				node = self.findRightMin(root.right)
				root.value = node.value
				root.right = self.delete(root.right, root.value)

		return root


	def inOrder(self, root):
		if not root:
			return []
		return self.inOrder(root.left) + [root.value] + self.inOrder(root.right)

	def preOrder(self, root):
		if not root:
			return []
		return [root.value] + self.inOrder(root.left) + self.inOrder(root.right)

	def levelOrder(self):
		result = []
		from collections import deque

		queue = deque()
		queue.append(self.root)
		result.append(self.root.value)
		while queue:
			node = queue.popleft()
			if node.left:
				queue.append(node.left)
				result.append(node.left.value)
			else:
				result.append(None)
			if node.right:
				queue.append(node.right)
				result.append(node.right.value)
			else:
				result.append(None)

		return result

	def __str__(self):
		inOrder = self.inOrder(self.root)
		result = ""
		for i in inOrder:
			result += str(i) + ","

		return result

if __name__ == "__main__":

	# [9, 2, 13, 1, 4, 10, 15, null, null, null, 8, null, null, null, null, 7, null, 5]

	bst = BST()
	bst.insert(9)
	bst.insert(2)
	bst.insert(4)
	bst.insert(8)
	bst.insert(13)
	bst.insert(7)
	bst.insert(1)
	bst.insert(5)
	bst.insert(10)
	bst.insert(15) #[9,2,4,8,13,7,1,5,10,15]
	bst.insert(3)
	# bst.insert(9, bst.root)
	# bst.insert(2, bst.root)
	# bst.insert(4, bst.root)
	# bst.insert(8, bst.root)
	# bst.insert(10, bst.root)
	# bst.insert(7, bst.root)
	# bst.insert(1, bst.root)
	# bst.insert(5, bst.root)
	# print(bst.preOrder(bst.root))
	print(bst.inOrder(bst.root))
	# print(bst.root)
	print(bst.levelOrder())
	bst.delete(bst.root, 9)
	bst.delete(bst.root, 13)
	print(bst.levelOrder())
	# print(bst.inOrder(bst.root))
	# print(bst.search(bst.root, 9))
	# print(bst.search(bst.root, 6))