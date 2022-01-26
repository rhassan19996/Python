from collections import deque
from queue import Queue
import random
from traceback import print_tb

q = deque()

for i in range(3):
  q.appendleft(random.randint(0,12))


while q:
  print(q.pop())

## Queue Dictionary

class Queue:
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self, val):
      self.buffer.appendleft(val)
    
    def dequeue(self):
      return self.buffer.pop()
    
    def is_empty(self):
      return len(self.buffer)==0
    
    def size(self):
      return len(self.buffer)
    
pq = Queue()

pq.enqueue({
  "company" : "Walmart",
  "TimeStamp" : "1/25/2020 9:00 pm",
  "Price" : 121
})
pq.enqueue({
  "company" : "Rog",
  "TimeStamp" : "1/25/2020 9:00 pm",
  "Price" : 1400
})
pq.enqueue({
  "company" : "Apple",
  "TimeStamp" : "1/25/2020 9:00 pm",
  "Price" : 200
})

print(pq.is_empty())
print(pq.size())

print(pq.buffer)

print(pq.dequeue())                