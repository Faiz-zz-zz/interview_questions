import random

class Node:
	def __init__(self, val):
		self.left = None
		self.right = None
		self.value = val

	def __repr__(self):
		return str(self.value)	

	def add(self, val):
		if val > self.value and self.right == None:
			self.right = Node(val)
		elif val <	self.value and self.left == None:
			self.left = Node(val)
		elif val > self.value and self.right is not None:
			self._add(val, self.right)	
		elif val < self.value and self.left is not None:
			self._add(val, self.left)

	def _add(self, val, node):
		if val > node.value and node.right == None:
			node.right = Node(val)
		elif val <	node.value and node.left == None:
			node.left = Node(val)
		elif val > node.value and node.right is not None:
			self._add(val, node.right)	
		elif val < node.value and node.left is not None:
			self._add(val, node.left)	

	def printTree(self):
		if self.value != None:
			print str(self.value)
			self._printTree(self.right)
			self._printTree(self.left)
	
	def _printTree(self, node):
			if node !=None:
				node.printTree()
			
			# node.right.printTree()		

tree = Node(50)

for i in range(100):
	tree.add(int(random.random()*100))

# print tree.left.right.right



tree.printTree()
