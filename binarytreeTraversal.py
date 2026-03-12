class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=' ')
        inorder(root.right)

def preorder(root):
    if root:
        print(root.data, end=' ')
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=' ')

def levelorder(root):
    if root is None:
        return
    queue = []
    queue.append(root)
    
    while queue:
        current = queue.pop(0)
        print(current.data, end=' ')
        
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)
root.right.right = node(6)

print("Inorder traversal:")
inorder(root)

print("\nPreorder traversal:")
preorder(root)

print("\nPostorder traversal:")
postorder(root)

print("\nLevel order traversal:")
levelorder(root)