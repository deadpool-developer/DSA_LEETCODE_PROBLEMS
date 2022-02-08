class Node:
    def __init__(self,data=0,left=None,right=None):
        self.data = data
        self.right= right
        self.left = left

root = Node(1,Node(2,Node(4),Node(5)), Node(3, Node(6),Node(7)))

def sumEven(root):
    if root:
        return (root.data if not root.data%2 else 0 ) + sumEven(root.left) + sumEven(root.right)
    return 0
    
print(sumEven(root))