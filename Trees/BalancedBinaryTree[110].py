#Given a binary tree, determine if it is height-balanced.

#For this problem, a height-balanced binary tree is defined as:

#a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

#Example 1:

#Input: root = [3,9,20,null,null,15,7]
#Output: true
#Example 2:

#Input: root = [1,2,2,3,3,null,null,4,4]
#Output: false
#Example 3:

#Input: root = []
#Output: true
 
#Constraints:
#The number of nodes in the tree is in the range [0, 5000].
#-104 <= Node.val <= 104

#CODE
def f(root):
    if root:
        l = f(root.left)
        r = f(root.right)
        return 1+max(l,r) if l is not None and r is not None and abs(l-r) < 2 else None
    return 0
class Solution(object):
    def isBalanced(self, root):
        return f(root) is not None
        