#Given the head of a singly linked list, return true if it is a palindrome.
#Example 1:
#Input: head = [1,2,2,1]
#Output: true

#Example 2:
#Input: head = [1,2]
#Output: false

#Constraints:
#The number of nodes in the list is in the range [1, 105].
#0 <= Node.val <= 9

#CODE

def cutinhalf(head):
    fast , slow = head.next, head
    if not fast:
        return None
    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next
    if fast.next:
        slow = slow.next
    x = slow.next
    slow.next = None
    return x

def reverse(head):
    if not head or not head.next:
        return head
    p,c,n = head, head.next, head.next.next
    p.next = None
    while n:
        c.next = p 
        p,c,n = c,n,n.next
    c.next = p
    return c

class Solution(object):
    def isPalindrome(self, head):
        h = cutinhalf(head)
        h = reverse(h)
        p = head
        while h:
            if p.val != h.val:
                return False
            p = p.next
            h = h.next
        return True