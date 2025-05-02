class LinkedList:
    def __init__(self):
        self.head = None
    
    
    def print_structure(self):
        current_node = self.head
        
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next