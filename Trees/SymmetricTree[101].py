#Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
#Example 1:

#Input: root = [1,2,2,3,4,4,3]
#Output: true
#Example 2:

#Input: root = [1,2,2,null,3,null,3]
#Output: false

#Constraints:

#The number of nodes in the tree is in the range [1, 1000].
#-100 <= Node.val <= 100

#CODE

class Solution(object):
    def isSymmetric(self, root):
        def f(root1, root2):
            if not root1 and not root2:
                return True
            if (root1 and not root2) or (root2 and not root1):
                return False
            if root1.val != root2.val:
                return False
            return f(root1.left, root2.right) and f(root1.right, root2.left)
        return f(root.left, root.right)