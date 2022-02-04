#You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

#You may assume the two numbers do not contain any leading zero, except the number 0 itself.

#Example 1:

#Input: l1 = [7,2,4,3], l2 = [5,6,4]
#Output: [7,8,0,7]
#Example 2:

#Input: l1 = [2,4,3], l2 = [5,6,4]
#Output: [8,0,7]

#Example 3:
#Input: l1 = [0], l2 = [0]
#Output: [0]

#Constraints:

#The number of nodes in each linked list is in the range [1, 100].
#0 <= Node.val <= 9
#It is guaranteed that the list represents a number that does not have leading zeros.

#CODE

class ListNode():
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next

def make_equal_len(l1,l2):
    k1, k2 = l1,l2
    while k1 or k2:
        (k1,l1) = (k1.next, l1) if k1 else (k1, ListNode(0,l1))
        (k2,l2) = (k2.next, l2) if k2 else (k2, ListNode(0,l2))
    return l1,l2
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        if not (l1.val and l2.val):
            return l2 if l2.val else l1
        l1, l2 = make_equal_len(l1,l2)
        any_l2 = True
        while any_l2:
            l1_p, l2_p, prev, any_l2 = l1, l2, None, False
            while l1_p:
                l1_p.val, l2_p.val  =(l1_p.val+l2_p.val)%10, (l1_p.val+l2_p.val)//10
                any_l2 = any_l2 or l2_p.val
                l1_p, l2_p, prev = l1_p.next, l2_p.next, l2_p
            prev.next = ListNode(0)
            (l1,l2) = (ListNode(0,l1),l2) if l2.val else (l1, l2.next)
        return l1
        