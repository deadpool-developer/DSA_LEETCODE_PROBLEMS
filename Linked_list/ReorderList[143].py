#You are given the head of a singly linked-list. The list can be represented as:

#L0 → L1 → … → Ln - 1 → Ln
#Reorder the list to be on the following form:

#L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
#You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 

#Example 1:


#Input: head = [1,2,3,4]
#Output: [1,4,2,3]
#Example 2:


#Input: head = [1,2,3,4,5]
#Output: [1,5,2,4,3]
 

#Constraints:

#The number of nodes in the list is in the range [1, 5 * 104].
#1 <= Node.val <= 1000

#CODE

def cutinhalf(head):
    fast, slow = head.next , head  #Using two pointers -> fast at one ahead of the slow 
    if not fast:  #if there is only one node i.e slow
        return None
    while fast.next and fast.next.next:  #untill we can jump two node with fast pointer
        fast = fast.next.next   #skips one node and point at second node
        slow = slow.next      #points next node
    if fast.next:   #when there is only one node at the end
        slow = slow.next #move only slow one step and the list got cut in two halves
    x = slow.next  #To cut the list in  two parts
    slow.next = None  #points next of slow to None
    return x   #returns the half cutted list

def reverse(head):
    if not head or not head.next:
        return head
    p, c, n = head , head.next, head.next.next
    p.next = None
    while n:
        c.next = p
        p,c,n = c,n,n.next
    c.next = p
    return c
    
class Solution(object):
    def reorderList(self, head):
        h = cutinhalf(head)  #head of the second half
        h = reverse(h)   #reverse the second half
        p = head   #head of the first half
        while h:   #runs untill the pointer reaches at the last node
            h2 = h.next   #stores the next node
            h.next = p.next  #points to the first half second node
            p.next = h    #points to the head of the second half
            p, h = p.next.next, h2  #skip p to +2 position and h to next node of the second half
        return head