class Node:
    def __init__(self,data=0,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

def printLeaf(root):
    if root:
        if not root.left and not root.right:
            print(root.data)
        printLeaf(root.left)
        printLeaf(root.right)

root = Node(1,Node(2,Node(4), Node(5)), Node(3,Node(6), Node(7)))
printLeaf(root)