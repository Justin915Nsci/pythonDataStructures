import tree
from queue import *


class binary_tree:
	def __init__(self,value):
		self.store =[value,None,None]
		
	def AddLeft(self,val):
		self.store[1] = val
		return True

	def AddRight(self,val):
		self.store[2] = val
		return True

	def Print_DepthFirst(self):
		self.PrintHLPR("    ")
		return True

	def PrintHLPR(self,prefix):
		print(prefix + str(self.store[0]))
		if self.store[1] != None:
			if type(self.store[1]) == int:
				print(prefix + prefix + str(self.store[1]))

			else:
				self.store[1].PrintHLPR(prefix + prefix + "")
		if self.store[2] != None:
			if type(self.store[2]) != binary_tree:
				print(prefix + prefix + str(self.store[2]))

			else:
				self.store[2].PrintHLPR(prefix + prefix + "")
		return True

	def GetLevelOrder(self):
		accum = ""
		q = queue()
		self.GloHlpr(q)
#		print(str(len(q.x)))
		for i in range(0,len(q.x),1):
			r = q.dequeue()
			accum = accum + str(r) + " "
		print(accum)		
		return True

	def GloHlpr(self, q):
		q.enqueue(self.store[0])
#		print(str(self.store[0]) +  "has been enqueued")
		if self.store[1] != None:
			self.store[1].GloHlpr(q)
		if self.store[2] != None:
			self.store[2].GloHlpr(q)
		return True
	
	def ConvertToTree(self):
		if len(self.store) > 3:
			return [False, None]
		x = self.CttHlpr()
		return [True, x]
		
	def CttHlpr(self):
		x = tree.tree(self.store[0])
#		print("self.store[1] is " + str(self.store[1]))
		if self.store[1] == None and self.store[2] == None:
			return tree.tree(self.store[0])
		
		x.AddSuccessor(self.store[1].CttHlpr())
		x.AddSuccessor(self.store[2].CttHlpr())
		return x

#class tree:
#	def __init__(self,x):
#		self.store = [x,[]]

def main():		
	x=binary_tree(1)
	x.AddLeft(binary_tree(2))
	y=binary_tree(3)
	y.AddLeft(binary_tree(4))
	y.AddRight(binary_tree(5))
	x.AddRight(y)
#	x.Print_DepthFirst()
#	x.GetLevelOrder()	
	t = x.ConvertToTree()
	if t[0] != False:
		t[1].Get_LevelOrder()

