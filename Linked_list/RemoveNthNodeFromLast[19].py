#Given the head of a linked list, remove the nth node from the end of the list and return its head.
#Example 1:
#Input: head = [1,2,3,4,5], n = 2
#Output: [1,2,3,5]

#Example 2:
#Input: head = [1], n = 1
#Output: []
#Example 3:
#Input: head = [1,2], n = 1
#Output: [1]

#Constraints:
#The number of nodes in the list is sz.
#1 <= sz <= 30
#0 <= Node.val <= 100
#1 <= n <= sz

#CODE

class Solution:
    def removeNthFromEnd(self, head, n: int):
        fast = head
        slow = head
        
		# let fast ptr travel n nodes first
        while fast and n > 0: #if n = 2 then fast reaches at 3
            fast = fast.next
            n -= 1
        
		# if fast is None, then we remove the first node
        if not fast:
            return head.next
        
		# let both fast and slow ptrs travel together
		# since fast ptr travelled n nodes alr
		# it means now the slow ptr will travel (L-n) nodes, thus nth node from end
        while fast:
            prev = slow
            fast = fast.next
            slow = slow.next
            
        prev.next = slow.next
        
        return head