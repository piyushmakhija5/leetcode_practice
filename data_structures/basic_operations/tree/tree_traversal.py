class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None
    
    def print_inOrder(self, root):
        print_inOrder(root.left)
        print(root.val)
        print_inOrder(root.right)

    def print_preOrder(self, root):
        print(root.val)
        print_preOrder(root.left)
        print_preOrder(root.right)

    def print_postOrder(self, root):
        print_postOrder(root.left)
        print_postOrder(root.right)
        print(root.val)

    if __name__ == "__main__":
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.right.right = Node(5)

        print_inOrder(root)
        print_preOrder(root)
        print_postOrder(root)