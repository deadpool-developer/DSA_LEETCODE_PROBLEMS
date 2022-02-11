#Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

#Example 1:

#Input: root = [1,2,3,null,5,null,4]
#Output: [1,3,4]
#Example 2:

#Input: root = [1,null,3]
#Output: [1,3]
#Example 3:

#Input: root = []
#Output: []

#Constraints:

#The number of nodes in the tree is in the range [0, 100].
#-100 <= Node.val <= 100

#CODE

def f(root,m,y):   #f(root , map , value)
    if root:
        m[y] = root.val     #first value will e=be of root at 0th index
        f(root.left , m , y+1)  #recursive call for left and update the value at the map index
        f(root.right , m, y+1)  #recursive call for right and update the value at the map index
class Solution(object):
    def rightSideView(self, root):
        m = dict()       #map
        f(root,m,0)      #0th index contain root value
        return m.values()  #return the values of the map at the end
        