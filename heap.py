class heap:
   def __init__(self):
      self.store = []
   

   def addHeap(self,val):
      self.store = self.store + [val]
      self.upHeap(len(self.store)-1)
      return True

   def upHeap(self,idx):
      if idx%2 == 0:
         pIdx = int((idx-2)/2)
      else:
        pIdx  = int((idx-1)/2)
#      print("pIdx is " + str(pIdx) )
      if idx == 0:
         return True

      if self.store[idx]>self.store[pIdx]:
         temp = self.store[pIdx]
         self.store[pIdx] = self.store[idx]
         self.store[idx] = temp
         self.upHeap(pIdx)
#      if self.store[idx] == 1000:
#         print("val at index " + str(pIdx) + "is " +str(self.store[pIdx]))
      return True

   def delHeap(self):
      if len(self.store)<1:
         return False

      ret = self.store[0]
      self.store[0] = self.store[len(self.store)-1]
      self.store = self.store[0:len(self.store)]
       

      return True

   def downHeap(self,idx):
      lIdx = (idx*2)+1
      rIdx = (idx*2)+2
      if lIdx >= len(self.store):
         return True
      if rIdx >=len(self.store):
         nIdx = lIdx
      else:
         if self.store[rIdx]>=self.store[lIdx]:
            nIdx = rIdx
         else:
            nIdx = lIdx
      temp = self.store[nIdx]
      self.store[nIdx] = self.store[idx]
      if self.store[idx] > self.store[nidx]:
         self.store[idx] = temp
         self.downHeap(nIdx)
      else:
         return True
      return True


