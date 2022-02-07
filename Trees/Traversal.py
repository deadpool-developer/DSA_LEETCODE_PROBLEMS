#Functions For Traversals in trees

from collections import deque


class Node:
    def __init__(self,data=0,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

root = Node(1,
                Node(2,Node(4),Node(5)),
                    Node(3,Node(6), Node(7)))

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")

def levelOrder(root):
    q = deque([root])
    while len(q):
        node = q.pop()
        print(node.data , end=" ")
        if node.left:
            q.appendleft(node.left)
        if node.right:
            q.appendleft(node.right)


print("Inorder")
inorder(root)
print("\nPreorder")
preorder(root)
print("\nPostorder")
postorder(root)
print("\nLevelOrder")
levelOrder(root)