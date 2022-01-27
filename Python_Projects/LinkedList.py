#implement a linked list from scratch

#create a class called node 
class Node():
    def __init__(self, data):
       self.data = data
       self.next = None

#linked list class that contains different funcctions
class LinkedList():
    def __init__(self, data):
        self.head = None
    #function that adds a node 
    def append(self, data):
      self.head = None
      new_node = Node(data)
    
    #checks if head exists and if it doesnt set head to new node
      if self.head is None:
        self.head = new_node
        return
    
    #traverse through the list
      last_node = self.head
      while last_node.next:
        last_node = last_node.next
      last_node.next = new_node
    
    
          
ll = LinkedList()
ll.append("A")
       
      
         