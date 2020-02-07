class room(object):
 def __init__(self,l,b,h):
     self.l, self.b,self.h=l,b,h
     def volume(self):
         return self.l*self.b*self.h
     obj2 = room(22,4,45)
     obj = volume()

