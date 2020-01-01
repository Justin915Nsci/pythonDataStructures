from queue import *
from stack import *


class graph:
   def __init__(self):
      self.store = []

   def addVertex(self,n):
      if n<1:
         return -1
      for i in range(0,n,1):
         self.store = self.store + []
      return len(self.store)

   def addEdge(self,from_idx,to_idx,directed,weight):
      if len(self.store)<from_idx or len(self.store)<to_idx:
         return False
      self.store[from_idx] = self.store[from_idx] + [to_idx]
      self.store[from_idx] = self.store[from_idx] + [weight]
      if directed == False:
         self.store[to_idx] = self.store[to_idx] + sef.store[from_idx]
         self.store[to_idx] = self.store[to_idx] + sef.store[weight]
      return True

   def traverse(self,start,typeBreadth):
      if typeBreadth == True:
         C = queue()
#      if typeBreadth == False:
      else:
         C = stack()
      ret = []
      Discovered = [False]*len(self.store)
      Processed = [False]*len(self.store)


      if start != None:
        v = start
      else:
         v = 0 
      for v in range(v,len(self.store),1):
         accum = []
 #        Discovered = [False]*len(self.store)
 #        Processed = [False]*len(self.store)
         if Discovered[v] == False:
            if typeBreadth == True:
               C.enqueue(v)
            else:
               C.push(v)
            Discovered[v] = True
         while(len(C.store)!=0):
            if typeBreadth == True:
               w = C.dequeue()
#               accum = accum + [w]
            else:
               w = C.pop()
 #              accum = accum + [w]
            connected = []
            if Processed[w] == False:
               accum = accum + [w]     
               Processed[w] = True
            for x in self.store[w]:
               if Discovered[x[0]] == False:
                  if typeBreadth == True:
                     C.enqueue(x[0])
                  else:
                     C.push(x[0])
                  Discovered[x[0]] = True                         
#            if len(C.store) == 0:
 #              break      

#         for k in range(0,len(Discovered),1):   
 #           if Discovered[k]==True:
  #             accum = accum + [k]           
         if len(accum)!=0:     
            ret = ret + [accum]
         if start != None:
            break           


      return ret

   def connectivity(self,vx,vy):
      way = self.traverse(vx,False)[0]
      Element = [False,False]
      for i in way:
#         print("i is " + str(i) + "and vy is " + str(vy))
         if i == vy:
            Element[0] = True
      way = self.traverse(vy,False)[0]
      
      for j in way:
         if j == vx:
            Element[1] = True
      return Element

   def path(self,vx,vy):
      Element = [[],[]]
      vertices =[]
      isPath = self.connectivity(vx,vy)
#      print(str(isPath))
      way = self.traverse(vx,False)
      if isPath[0] == True:
         vertices = vertices + [vx]
         steps = self.store[vx]
         nxt = vx
         while(True):
            steps = self.store[nxt]
            for i in steps:
#               print("i[0] is " + str(i[0]) +  " and vy is " + str(vy) )
               if i[0] == vy:
                  vertices = vertices + [i[0]]
                  break
               connect = self.connectivity(i[0],vy)
#               print(str(connect))
               if connect[0] == True:
                  vertices = vertices + [i[0]]
            if i[0] == vy:
               break
            nxt = nxt + 1                                   
         Element[0] = vertices                        

      if isPath[1] == True:
         vertices = vertices + [vy]
         steps = self.store[vy]
         nxt = vy
         while(True):
            steps = self.store[nxt]
            for j in steps:
#               print("i[0] is " + str(i[0]) +  " and v
               if j[0] == vx:
                  vertices = vertices + [j[0]]
                  break
               connect = self.connectivity(j[0],vx)
#               print(str(connect))
               if connect[0] == True:
                  vertices = vertices + [j[0]]
            if j[0] == vx:
               break
            nxt = nxt + 1                              
         Element[1] = vertices                        

                                   

      return Element


      
x = graph()
x.store = [[[1,5],[3,-10]],[[0,3]],[],[],[[2,10]]]
print(str(x.traverse(None,False)))
#print(str(x.path(0,1)))            
      
