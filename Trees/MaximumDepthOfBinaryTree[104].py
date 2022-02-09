#Given the root of a binary tree, return its maximum depth.

#A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

#Example 1:

#Input: root = [3,9,20,null,null,15,7]
#Output: 3
#Example 2:

#Input: root = [1,null,2]
#Output: 2
 

#Constraints:

#The number of nodes in the tree is in the range [0, 104].
#-100 <= Node.val <= 100

#CODE

def f(root):
    if not root:   #if their is no root
        return 0
    if root:  #if root is present
        if not (root.left or root.right):   #if root left and right is not present return 1
            return 1
        return max(f(root.left) , f(root.right)) + 1   #return max of left or right and add 1 for root node in it

class Solution(object):
    def maxDepth(self, root):
        return f(root)    #call the function
        