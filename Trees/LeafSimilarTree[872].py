#Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.

#For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

#Two binary trees are considered leaf-similar if their leaf value sequence is the same.

#Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

#Example 1:

#Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
#Output: true
#Example 2:

#Input: root1 = [1,2,3], root2 = [1,3,2]
#Output: false
 
#Constraints:

#The number of nodes in each tree will be in the range [1, 200].
#Both of the given trees will have values in the range [0, 200].

#CODE

#1 Little bit inefficient code

def getseq(root):
    if root:        #if root is not null
        if not (root.left or root.right):   #if no root.left and not root.right 
            return [root.val]               #return the root value
        return getseq(root.left) + getseq(root.right)  #else return the leaf nodes from right and left
    return []                                        #else return the empty list
class Solution(object):
    def leafSimilar(self, root1, root2):
        return getseq(root1) == getseq(root2)        #if root1 leaf list == root2 leaf list return True


#2 efficent code using append function and global variable ans

ans = None
def getseq(root):
    if root:
        if not (root.left or root.right):
            ans.append(root.val)
        else:
            getseq(root.left)
            getseq(root.right)
class Solution(object):
    def leafSimilar(self,root1,root2):
        global ans
        ans =[]
        getseq(root1)
        t = ans[:]
        ans =[]
        getseq(root2)
        return ans == t