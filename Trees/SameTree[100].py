#Given the roots of two binary trees p and q, write a function to check if they are the same or not.

#Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

#Example 1:

#Input: p = [1,2,3], q = [1,2,3]
#Output: true
#Example 2:

#Input: p = [1,2], q = [1,null,2]
#Output: false
#Example 3:

#Input: p = [1,2,1], q = [1,1,2]
#Output: false
 
#Constraints:

#The number of nodes in both trees is in the range [0, 100].
#-104 <= Node.val <= 104

#CODE

class Solution(object):
    def isSameTree(self, p, q):
        #if p and q are both Null
        if not p and not q:
            return True
        #if p or q one of this is Null
        if not p or not q:
            return False
        #if value of p and q are not equal
        if p.val != q.val:
            return False
        #Check if left of p and left of q is same and right respectively
        l = self.isSameTree(p.left,q.left)
        r = self.isSameTree(p.right,q.right)
        return l and r