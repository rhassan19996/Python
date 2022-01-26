#this program is used to rder food and serve order using the 
#queue data structures FIFO principles
from collections import deque

class Queue:
  def __init__(self):
    self.buffer = deque()
  
  def enqueue(self, val):
    self.buffer.appendleft(val)
  
  def dequeue(self):
    return self.buffer.pop()
  
  def is_empty(self):
    return len(self.buffer) == 0
  
  def size(self):
    return len(self.buffer)

pq = Queue()

def PlaceOrder(orders):
  for order in orders:
    print ("placing order for: " , order)
    pq.enqueue(order)
    
    

def Serveorder():
  while pq.is_empty() == False:
    order = pq.dequeue()
    print("Now serving: ", order)
    

if __name__ == '__main__':
    orders = ['pizza','samosa','pasta','biryani','burger']
    
  


PlaceOrder(orders)
Serveorder()   
      
       
      
      