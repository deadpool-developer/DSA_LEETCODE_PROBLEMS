#Functions For Traversals in trees

from collections import deque
from distutils.dir_util import copy_tree


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

#This tell the node present at every level which can not be signify by the levelOrder
def levelOrder2(root):
    q = deque([None,root])   #Insert Dummy value after each level ends ->None
    while True:   #Till q is not empty
        node = q.pop()   #pop the element
        if not node:   #if there of no node left inside the tree
            if len(q) <1:   #check if the length of the tree is less than 1
                return   #return the list
            print("")   #next line
            q.appendleft(None)   #After each level insert Dummy Node inside the queue
            continue    #continue 
        print(node.data,end=" ")   #print the data of the tree
        if node.left:    #if there is nodes present in the left of the tree
            q.appendleft(node.left)     #append in the left
        if node.right:     #if present in the right
            q.appendleft(node.right)  #append it

def levelOrderListofList(root):
    q  =deque([None,root])
    curr = []
    ans = []
    while True:
        node = q.pop()
        if not node:
            ans.append(curr)
            if len(q) < 1:
                print(ans)
                return
            curr =[]
            q.appendleft(None)
            continue
        curr.append(node.data)
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
print("\nLevelOrder2")
levelOrder2(root)
print("\nLevelOrderListofList")
levelOrderListofList(root)