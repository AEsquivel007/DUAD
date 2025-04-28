class Node:
    def __init__(self, data: str):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    root: Node
    
    def __init__(self):
        self.root = None
    
    
    def append(self, data:str):
        new_node = Node(data)
        
        if self.root is None:
            self.root = new_node
        else:
            self._insert(self.root, data)
    
    
    def _insert(self, current_node: Node, data:str):
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self._insert(current_node.left, data)
        elif data >= current_node.data:
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self._insert(current_node.right, data)
    
    def print_structure(self, node: Node):
        if node:
            self.print_structure(node.left)
            print(node.data)
            self.print_structure(node.right)

#Execution:
b_tree = BinaryTree()

print("/*************************/")
print("Working with binary trees...!!!")
b_tree.append("Elephant")
b_tree.append("Dinosaur")
b_tree.append("Light")
b_tree.append("Day")
b_tree.append("Dust")
b_tree.append("Nintendo")
#b_tree.append("Mammoth")
b_tree.append("Gate")
#b_tree.append("Table")

print("/*************************/")
b_tree.print_structure(b_tree.root)