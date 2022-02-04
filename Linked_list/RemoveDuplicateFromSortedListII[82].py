#Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
#Return the linked list sorted as well.

#Input: head = [1,2,3,3,4,4,5]
#Output: [1,2,5]
#Example 2:


#Input: head = [1,1,1,2,3]
#Output: [2,3]
 

#Constraints:

#The number of nodes in the list is in the range [0, 300].
#-100 <= Node.val <= 100
#The list is guaranteed to be sorted in ascending order.

#CODE

class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        if not head:
            return head
        head = p = ListNode(0, head)
        l = r = head.next
        while r:
            if r.val == l.val:
                r = r.next
            elif l.next is r:
                p.next = l
                p = p.next
                l = r
            else:
                l = r
        p.next = None if l.next else l
        return head.next