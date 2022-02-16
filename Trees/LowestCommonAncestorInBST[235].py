#Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

#According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

#Example 1:

#Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
#Output: 6
#Explanation: The LCA of nodes 2 and 8 is 6.
#Example 2:


#Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
#Output: 2
#Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
#Example 3:

#Input: root = [2,1], p = 2, q = 1
#Output: 2
 

#Constraints:

#The number of nodes in the tree is in the range [2, 105].
#-109 <= Node.val <= 109
#All Node.val are unique.
#p != q
#p and q will exist in the BST.

#CODE
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if root == None:        #if there is no root
            return root        #return the root
        #if p.val is smaller than the root and the q.val is greater than the root or vice versa
        if (p.val <= root.val and q.val >= root.val) or (p.val >= root.val and q.val <= root.val):
            return root
        #if p.val is greater than the root and the q.val is smalller than the root
        elif p.val <=root.val and q.val <= root.val:
            root = self.lowestCommonAncestor(root.left,p,q)
        else:
            root = self.lowestCommonAncestor(root.right,p,q)
        return root      #return root