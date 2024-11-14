# height of the binary tree with root p.
def height(node):
    if node is None:
        return 0
    else:
        return 1 + max(height(node.left), height(node.right))


class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def height(node):
    if node is None:
        return 0
    else:
        return 1 + max(height(node.left), height(node.right))
    
# Insert Operation 
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def copy_tree(copied_tree_root, other_tree_root):
    if other_tree_root is None:
        copied_tree_root = None
    else:
        copied_tree_root = BinaryTreeNode(other_tree_root.value)
        copied_tree_root.left = copy_tree(copied_tree_root.left, other_tree_root.left)
        copied_tree_root.right = copy_tree(copied_tree_root.right, other_tree_root.right)
    
    return copied_tree_root

# Search Operation
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            # If the tree is empty, create the root node
            self.root = BinaryTreeNode(data)
            return
        
        # Start from the root and find the correct position for the new data
        current = self.root
        while True:
            # If data is greater, go to the right subtree
            if data > current.value:
                if current.right is None:
                    # Insert here if right child is None
                    current.right = BinaryTreeNode(data)
                    break
                else:
                    # Otherwise, move to the right child
                    current = current.right
            # If data is smaller, go to the left subtree
            else:
                if current.left is None:
                    # Insert here if left child is None
                    current.left = BinaryTreeNode(data)
                    break
                else:
                    # Otherwise, move to the left child
                    current = current.left
                    

class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def search(self, data):
        # Start the search from the root node
        current = self.root
        
        while current is not None:
            # If the current node's value matches the search data, return the node
            if current.value == data:
                return current
            # If the search data is greater, move to the right subtree
            elif data > current.value:
                current = current.right
            # If the search data is smaller, move to the left subtree
            else:
                current = current.left
        
        # If the loop exits, the data was not found
        return "Data not found"
    
# Binary Tree Traversal
class Node:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        newNode = Node(data)
        # If the tree is empty, set root to the new node
        if self.root is None:
            self.root = newNode
        else:
            current = self.root
            while True:
                parent = current
                # If data is less, go to the left subtree
                if data < current.data:
                    current = current.leftChild
                    # If the spot is empty, insert the new node
                    if current is None:
                        parent.leftChild = newNode
                        return
                # Otherwise, go to the right subtree
                else:
                    current = current.rightChild
                    # If the spot is empty, insert the new node
                    if current is None:
                        parent.rightChild = newNode
                        return

    def search(self, data):
        current = self.root
        print("Visiting elements: ", end="")

        while current is not None:
            print(current.data, end=" ")
            if current.data == data:
                print("\n")
                return current
            elif data < current.data:
                current = current.leftChild
            else:
                current = current.rightChild

        print("\n")
        return None

    def pre_order_traversal(self, root):
        if root:
            print(root.data, end=" ")
            self.pre_order_traversal(root.leftChild)
            self.pre_order_traversal(root.rightChild)

    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.leftChild)
            print(root.data, end=" ")
            self.inorder_traversal(root.rightChild)

    def post_order_traversal(self, root):
        if root:
            self.post_order_traversal(root.leftChild)
            self.post_order_traversal(root.rightChild)
            print(root.data, end=" ")
            
# Search Operation
class Node:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def search(self, data):
        current = self.root
        print("Visiting elements: ", end="")

        while current is not None:
            print(current.data, end=" ")
            # If the current node's data matches the search data, return the node
            if current.data == data:
                print("\n")  # Newline after visiting elements
                return current
            # Go to the left subtree if data is smaller than current node's data
            elif data < current.data:
                current = current.leftChild
            # Go to the right subtree if data is greater than current node's data
            else:
                current = current.rightChild

        # If loop exits, data was not found
        print("\n")
        return None
    

# Insert Operation
class Node:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)
        # If the tree is empty, set the root to the new node
        if self.root is None:
            self.root = new_node
            return
        else:
            current = self.root
            parent = None

            # Traverse the tree to find the correct insertion point
            while True:
                parent = current
                # Go to the left subtree if data is smaller
                if data < parent.data:
                    current = current.leftChild
                    # If there is no left child, insert here
                    if current is None:
                        parent.leftChild = new_node
                        return
                # Go to the right subtree if data is larger or equal
                else:
                    current = current.rightChild
                    # If there is no right child, insert here
                    if current is None:
                        parent.rightChild = new_node
                        return