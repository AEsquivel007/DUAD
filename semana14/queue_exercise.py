from node import Node
from linked_list import LinkedList

class Queue(LinkedList):
    
    def enqueue(self, data):
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
        else:
            current_node = self.head
            
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
    
    
    def dequeue(self):
        
        if not self.head:
            raise IndexError("[WARNING]: Empty queue, dequeue action is not allowed.!!!")
        dequeued_node = self.head.data
        self.head = self.head.next
        return dequeued_node

#Execution:
queue = Queue()

print("/*************************/")
print("Working with queues...!!!")

queue.enqueue("First node")
queue.enqueue("Second node")
queue.enqueue("Third node")
print("/*************************/")
queue.print_structure()
print("/*************************/")
print(f"Dequeued: {queue.dequeue()}")
queue.enqueue("Fourth node")
print("/*************************/")
queue.print_structure()