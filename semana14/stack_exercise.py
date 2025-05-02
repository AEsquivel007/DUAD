from node import Node

class Stack:
    top: Node
    
    def __init__(self):
        self.top = None
    
    
    def push(self, data:str):
        new_node = Node(data)
        
        if not self.top:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
    
    
    def pop(self):
        if not self.top:
            raise IndexError("[WARNING]: Empty stack, pop action is not allowed.!!!")
        data = self.top.data
        self.top = self.top.next
        
        return data
    
    
    def print_structure(self):
        current_node = self.top
        
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next


#Execution:
stack = Stack()

print("/*************************/")
print("Working with stacks...!!!")
stack.push("First node")
stack.push("Second node")
stack.push("Third node")
print("/*************************/")
stack.print_structure()
print("/*************************/")
print(f"Popped: {stack.pop()}")
print("/*************************/")
stack.print_structure()