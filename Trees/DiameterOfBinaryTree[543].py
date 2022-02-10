#Given the root of a binary tree, return the length of the diameter of the tree.

#The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

#The length of a path between two nodes is represented by the number of edges between them.

#Example 1:

#Input: root = [1,2,3,4,5]
#Output: 3
#Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
#Example 2:

#Input: root = [1,2]
#Output: 1
 
#Constraints:

#The number of nodes in the tree is in the range [1, 104].
#-100 <= Node.val <= 100

#CODE

def f(root):
    if root:
        ld,lp = f(root.left)  #ld -> left depth & lp-> left path
        rd,rp = f(root.right) #rd -> right depth & rp -> right path
        return 1+ max(ld,rd) , max(lp,rp,1+ld+rd)  #return max depth , max path
    return 0 , 0                                    #else return 0 -> depth, 0 -> path
class Solution:
    def diameterOfBinaryTree(self, root):
        return f(root)[1] - 1   #return the second argument - 1 -> number of links 