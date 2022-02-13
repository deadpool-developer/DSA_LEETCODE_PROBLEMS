#Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

#Basically, the deletion can be divided into two stages:

#Search for a node to remove.
#If the node is found, delete the node.
 
#Example 1:

#Input: root = [5,3,6,2,4,null,7], key = 3
#Output: [5,4,6,2,null,null,7]
#Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
#One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
#Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

#Example 2:

#Input: root = [5,3,6,2,4,null,7], key = 0
#Output: [5,3,6,2,4,null,7]
#Explanation: The tree does not contain a node with value = 0.
#Example 3:

#Input: root = [], key = 0
#Output: []
 

#Constraints:

#The number of nodes in the tree is in the range [0, 104].
#-105 <= Node.val <= 105
#Each node has a unique value.
#root is a valid binary search tree.
#-105 <= key <= 105

#CODE
class Solution:
    def deleteNode(self, root,key):
        # Base Case:
        if not root:
            return None
        # Eliminate half of possible tree nodes
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # No child, leaf
            if (not root.left) and (not root.right):
                return None
            # One child
            elif (root.left) and (not root.right): # Only left child
                root = root.left
            elif (not root.left) and (root.right): # Only right child
                root = root.right
            # Two children
            else:
                minValue = self.findNextMin(root.right)
                root.val = minValue
                root.right = self.deleteNode(root.right, minValue)
        return root
    
    def findNextMin(self, root):
        # Keep root val
        result = root.val
        # Dive into deepest level, find the most left child
        while root.left:
            root = root.left
            result = root.val
        return result
        