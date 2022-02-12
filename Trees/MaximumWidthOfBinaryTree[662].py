#Given the root of a binary tree, return the maximum width of the given tree.

#The maximum width of a tree is the maximum width among all levels.

#The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes are also counted into the length calculation.

#It is guaranteed that the answer will in the range of 32-bit signed integer.

#Example 1:

#Input: root = [1,3,2,5,3,null,9]
#Output: 4
#Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
#Example 2:

#Input: root = [1,3,null,5,3]
#Output: 2
#Explanation: The maximum width existing in the third level with the length 2 (5,3).
#Example 3:


#Input: root = [1,3,2,5]
#Output: 2
#Explanation: The maximum width existing in the second level with the length 2 (3,2).

#CODE
def getw(root, rootlevel, rootindex, widthmap):
    if root:
        if rootlevel not in widthmap:
            widthmap[rootlevel] = [rootindex , rootindex]
        elif rootindex < widthmap[rootlevel][0]:
            widthmap[rootlevel][0] = rootindex
        elif rootindex > widthmap[rootlevel][1]:
            widthmap[rootlevel][1] = rootindex
        getw(root.left , rootlevel +1 , (2*rootindex) + 1, widthmap)
        getw(root.right, rootlevel +1 , (2*rootindex)+2 , widthmap)
class Solution(object):
    def widthOfBinaryTree(self, root):
        widthmap = {}
        getw(root , 0, 0, widthmap)
        return max([1+ x[1] - x[0] for x in widthmap.values()])