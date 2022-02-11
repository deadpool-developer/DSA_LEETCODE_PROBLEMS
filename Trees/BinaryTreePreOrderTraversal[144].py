#Given the root of a binary tree, return the preorder traversal of its nodes' values.

#Example 1:

#Input: root = [1,null,2,3]
#Output: [1,2,3]
#Example 2:

#Input: root = []
#Output: []
#Example 3:

#Input: root = [1]
#Output: [1]
 
#Constraints:

#The number of nodes in the tree is in the range [0, 100].
#-100 <= Node.val <= 100

#CODE

#RECURSIVE APPROACH
class Solution(object):
    def preorderTraversal(self, root):
        if not root:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
        
#ITERATIVE APPROACH
class Solution(object):
    def preorderTraversal(self, root):
        queue = [root]
        lst = []
        while queue != []:
            node = queue.pop()
            if node:
                lst.append(node.val)
                queue.append(node.right)
                queue.append(node.left)
                
        return lst
        