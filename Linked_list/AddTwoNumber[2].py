#You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
#You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#Example 1:


#Input: l1 = [2,4,3], l2 = [5,6,4]
#Output: [7,0,8]
#Explanation: 342 + 465 = 807.
#Example 2:

#Input: l1 = [0], l2 = [0]
#Output: [0]
#Example 3:

#Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
#Output: [8,9,9,9,0,0,0,1]
 

#Constraints:

#The number of nodes in each linked list is in the range [1, 100].
#0 <= Node.val <= 9
#It is guaranteed that the list represents a number that does not have leading zeros.

#CODE

 #Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0 #intialize carry to 0
        ans = p = ListNode() #Storing the dummy node in the answer 
        while l1 and l2: #until one of the l1 or l2 ends
            k = l1.val + l2.val + carry  #stores the sum value of the first node in both the lists
            p.next = ListNode(k%10)  #Store the first value of the number i.e 13 -> 3
            carry = k//10  #store the tens place value i.e 13-> 1
            p , l1, l2 = p.next , l1.next, l2.next  #incrementing
        if l2:
            l1 = l2  #Stores the l2 remaining value in l1 so as to use only one loop
        while l1:  #for remaining node elements
            k = l1.val + carry  #stores the sum
            p.next = ListNode(k % 10)  #Store the First value of the number
            carry = k//10  #Store the tens place value of the number
            p , l1 = p.next, l1.next   #incrementing
        if carry:   #if carry != 0 
            p.next = ListNode(carry)  #Add a node for the carry at the end
            
        return ans.next  #return the next of the answer as at first dummy node is used