#Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.
 

#Example 1:


#Input: root = [3,9,20,null,null,15,7]
#Output: [3.00000,14.50000,11.00000]
#Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
#Hence return [3, 14.5, 11].
#Example 2:


#Input: root = [3,9,20,15,7]
#Output: [3.00000,14.50000,11.00000]
 

#Constraints:

#The number of nodes in the tree is in the range [1, 104].
#-231 <= Node.val <= 231 - 1

#CODE
from collections import deque
class Solution(object):
    def averageOfLevels(self, root):
        q = deque([None,root])        
        ans = []
        curr = []
        while True:
            node = q.pop()      #pop the element from the queue and insert it in the node
            if not node:        #if there is no node
                ans.append(float(sum(curr))/len(curr))   #average of the node at each level
                if len(q) < 1:       #if queue is empty
                    return ans       #return the list
                curr = []            #empty the curr list
                q.appendleft(None)   #append None value after every level ends
                continue
            curr.append(node.val)    #append the node value in the curr
            if node.left:
                q.appendleft(node.left)  #if left append
            if node.right:
                q.appendleft(node.right)  #if right appenda