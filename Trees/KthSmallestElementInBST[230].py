#Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

#Example 1:

#Input: root = [3,1,4,null,2], k = 1
#Output: 1
#Example 2:

#Input: root = [5,3,6,2,4,null,null,1], k = 3
#Output: 3
 
#Constraints:
#The number of nodes in the tree is n.
#1 <= k <= n <= 104
#0 <= Node.val <= 104
 
#Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?

#CODE
class Solution(object):
    def ino(self,root):
        if not root:     #check if there is root or not, if not return the empty list
            return []
        l , r = self.ino(root.left), self.ino(root.right)   #store left tree in the l and right of the tree in the r
        return l + [root.val] + r         #return the inorder of the BST
    def kthSmallest(self, root, k): 
        nums = self.ino(root)      #store the inorder list in the nums
        return nums[k-1]           #return the value at the (k-1)th index
         