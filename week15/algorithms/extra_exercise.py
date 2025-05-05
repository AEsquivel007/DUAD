class Node:
    def __init__(self, data:int, next = None):
        self.data = data
        self.next = next


class LinkedList:
    head: Node
    
    def __init__(self, head:Node):
        self.head = head
    
    
    def print_structure(self):
        current_node = self.head
        
        while current_node:
            print(current_node.data)
            current_node = current_node.next
    
    
    def obtain_length(self):
        length = 0
        current_node = self.head
        
        while current_node:
            length += 1
            current_node = current_node.next
        return length
    
    
    def sort_linked_list(self):
        length = self.obtain_length()
        
        for iteration in range(0, length):
            current_node = self.head
            next_node = current_node.next
            has_made_changes = False
            
            print(f"Iteration: {iteration + 1}...!!!")
            
            while current_node.next:
            
                if current_node.data > next_node.data:
                    print(f"Switching data among nodes...")
                    current_data = current_node.data
                    next_data = next_node.data
                    
                    current_node.data = next_data
                    current_node.next.data = current_data
                    has_made_changes = True
                current_node = current_node.next
                next_node = current_node.next
            
            if not has_made_changes:
                return


#Execution:

print("/*************************/")
print("Working with LinkedList and bubble sort algorithm..!!!")

seventh_node = Node(30)
sixth_node = Node(25,seventh_node)
fifth_node = Node(100,sixth_node)
fourth_node = Node(1,fifth_node)
third_node = Node(8, fourth_node)
second_node = Node(15, third_node)
first_node = Node(10, second_node)

linked_list = LinkedList(first_node)
linked_list.print_structure()
linked_list.sort_linked_list()
linked_list.print_structure()