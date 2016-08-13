import random

class Node:
	def __init__(self, val):
		self.left = None
		self.right = None
		self.value = val

class Tree:
	def __init__(self):
		self.root = None

	def getRoot(self):
		return self.root	
	
	def add(self, val):
		if (self.getRoot == None):
			self.root = Node(val)
		else:
			self.addLeaves(val, self.root)

	def addLeaves(self, val, Node):
		if ( val < Node.value ):
			if ( Node.left != None ):
				self.addLeaves(val, Node.left)
			else:
				Node.left = Node(val)
		else:
			if ( Node.right != None):
				self.addLeaves(val, Node.right)
			else:
				Node.ight = Node(val)

	def find(self, val):
		if (self.root != None):
			return findVal(val, self.root)
		else:
			return None

	def findVal(self, val, Node):
		if (val == Node.value):
			return Node
		elif (val < Node.left and Node.left != None):
			return findVal(val, Node.left)
		elif (val > Node.right and Node.right != None):
			return findVal(val, Node.right)


tree = Tree()

for i in range(100):
	tree.add(random.random()*100)

tree.find(1)	
