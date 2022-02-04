#Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head.

#The steps of the insertion sort algorithm:

#Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.
#At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list and inserts it there.
#It repeats until no input elements remain.
#The following is a graphical example of the insertion sort algorithm. The partially sorted list (black) initially contains only the first element in the list. One element (red) is removed from the input data and inserted in-place into the sorted list with each iteration.


 

#Example 1:


#Input: head = [4,2,1,3]
#Output: [1,2,3,4]
#Example 2:


#Input: head = [-1,5,3,4,0]
#Output: [-1,0,3,4,5]
 

#Constraints:

#The number of nodes in the list is in the range [1, 5000].
#-5000 <= Node.val <= 5000

#CODE

class ListNode():
    def __init__(self,val=0, next = None):
        self.val = val
        self.next = next

class Solution(object):
    def insertionSortList(self, head):
        if not head or not head.next:
            return head
        dummy = ListNode(val = -5000, next = head)  #dummy node
        last_node = head  #pointing to first node of list
        cur = head.next   #pointing the second node of the head.next
        while cur:        #till the cur become None
            if cur.val >= last_node.val:   #cur value if greater than the previous node value
                last_node = last_node.next #shift last_node to next
            else:
                prev = dummy   #starting from the dummy node in linked list
                while prev.next.val <= cur.val:  #if head.val is less than to cur.val
                    prev = prev.next   #increment it and check with next node
                last_node.next = cur.next  #last_node k next ko point krdo cur.next ko
                cur.next = prev.next   #cur.next ko prev k next ko point krdo
                prev.next = cur  #prev k next ko cur pr point krdo 
            cur = last_node.next  #increment current and place it next to last_node
        return dummy.next  #return dummy.next

