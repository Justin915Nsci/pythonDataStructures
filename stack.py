class stack:
   def __init__(self):
      self.store = []
   def push(self,val):
      self.store = self.store + [val]
      return True
   def pop(self):
      if len(self.store) == 0:
         print("The stack is empty.")
         return False
      rem = self.store[len(self.store)-1]
      self.store = self.store[0:len(self.store)-1]
      return rem
