#You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

#Merge all the linked-lists into one sorted linked-list and return it.

#Example 1:

#Input: lists = [[1,4,5],[1,3,4],[2,6]]
#Output: [1,1,2,3,4,4,5,6]
#Explanation: The linked-lists are:
#[
#  1->4->5,
#  1->3->4,
#  2->6
#]
#merging them into one sorted list:
#1->1->2->3->4->4->5->6
#Example 2:

#Input: lists = []
#Output: []
#Example 3:

#Input: lists = [[]]
#Output: []
 

#Constraints:

#k == lists.length
#0 <= k <= 104
#0 <= lists[i].length <= 500
#-104 <= lists[i][j] <= 104
#lists[i] is sorted in ascending order.
#The sum of lists[i].length will not exceed 104.

#CODE

import heapq
class ListNode(object):
    pass
class Solution(object):
    def mergeKLists(self, lists):
        heap = []
        for head in lists:
            if head:
                heapq.heappush(heap , (head.val , head))
        ans = ListNode()
        p = ans
        while len(heap) > 0:
            n = heapq.heappop(heap)[1]
            p.next = n
            p = n
            if n.next:
                heapq.heappush(heap , (n.next.val , n.next))
        return ans.next
        