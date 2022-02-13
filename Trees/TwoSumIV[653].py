#Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST
#such that their sum is equal to the given target.

#Example 1:

#Input: root = [5,3,6,2,4,null,7], k = 9
#Output: true
#Example 2:

#Input: root = [5,3,6,2,4,null,7], k = 28
#Output: false
 
#Constraints:

#The number of nodes in the tree is in the range [1, 104].
#-104 <= Node.val <= 104
#root is guaranteed to be a valid binary search tree.
#-105 <= k <= 105

#CODE

#1. Converting the tree into inorder sequence and then using two pointers approach

def ino(l,root):
    if root:
        ino(l,root.left)
        l.append(root.val)
        ino(l,root.right)
class Solution(object):
    def findTarget(self, root, k):
        nums = []
        ino(nums,root)
        l,r = 0, len(nums) - 1
        while l < r:
            s = nums[l] + nums[r]
            if s < k:
                l += 1
            elif s > k:
                r -= 1
            else:
                return True
        return False
        
#2. 