#Given the head of a singly linked list, reverse the list, and return the reversed list.

#Example 1:
#Input: head = [1,2,3,4,5]
#Output: [5,4,3,2,1]

#Example 2:
#Input: head = [1,2]
#Output: [2,1]
#Example 3:
#Input: head = []
#Output: []

#Constraints:
#The number of nodes in the list is the range [0, 5000].
#-5000 <= Node.val <= 5000

#CODE

class Solution(object):
    def reverseList(self, head):
        if not head or not head.next:    #if no node or having single node
            return head
        p,c,n = head , head.next , head.next.next
        p.next = None   #points head.next -> None, means head is at last of the list
        while n:        #until None occur
            c.next = p  
            p = c
            c= n 
            n = n.next
        c.next = p      
        return c
        