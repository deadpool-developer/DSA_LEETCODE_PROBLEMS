class Node:
    def __init__(self,data = 0, left = None, right = None):
        self.data = data
        self.left =left
        self.right = right

root = Node(1,Node(2,Node(4), Node(5)), Node(3,Node(6), Node(7)))

#sum of all nodes
def sumall(root):
    if root:
        return root.data + sumall(root.left) + sumall(root.right)
    return 0

# def sumleaf(root):
#     if root:
#         if not root.left and not root.right:
#             return root.data
#         return sumleaf(root.left) + sumleaf(root.right)
#     return 0

#Sum of leaf nodes
def sumleaf(root):
    if not root.left and not root.right:
        return root.data
    sum = sumleaf(root.left) if root.left else 0
    sum += sumleaf(root.right) if root.right else 0
    return sum

print(sumall(root))
print(sumleaf(root))