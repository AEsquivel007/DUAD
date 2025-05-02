from node import Node

class DoubleEndedQueue:
    head: Node
    tail: Node
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    
    def push_left(self, data:str):
        new_node = Node(data)
        
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    
    
    def push_right(self, data: str):
        new_node = Node(data)
        
        if not self.tail:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    
    
    def pop_left(self):
        if not self.head:
            raise IndexError("[WARNING]: Empty double ended queue, pop-left action is not allowed.!!!")
        
        elif self.head == self.tail:
            data = self.head.data
            self.head = self.tail = None
            
            return data
        
        else:
            data = self.head.data
            self.head = self.head.next
            
            return data
    
    
    def pop_right(self):
        if not self.tail:
            raise IndexError("[WARNING]: Empty double ended queue, pop-right action is not allowed.!!!") 
        
        elif self.head == self.tail:
            data = self.head.data
            self.head = self.tail = None
            
            return data
        
        else:
            current_node = self.head
            
            while current_node.next != self.tail:
                current_node = current_node.next
            
            data = self.tail.data
            self.tail = current_node
            self.tail.next = None
            
            return data
    
    def print_structure(self):
        current_node = self.head
        
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next


#Execution:
deque = DoubleEndedQueue()

print("/*************************/")
print("Working with deques...!!!")
deque.push_left("First node")
deque.push_left("Second node")
deque.push_right("Third node")
deque.push_left("Fourth node")
deque.push_right("Fifth node")
print("/*************************/")
deque.print_structure()
print("/*************************/")
print(f"Popped left: {deque.pop_left()}")
print("/*************************/")
deque.print_structure()
print("/*************************/")
print(f"Popped right: {deque.pop_right()}")
print("/*************************/")
deque.print_structure()