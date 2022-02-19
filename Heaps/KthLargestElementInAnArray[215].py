#Given an integer array nums and an integer k, return the kth largest element in the array.

#Note that it is the kth largest element in the sorted order, not the kth distinct element.

#Example 1:

#Input: nums = [3,2,1,5,6,4], k = 2
#Output: 5
#Example 2:

#Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
#Output: 4
 
#Constraints:

#1 <= k <= nums.length <= 104
#-104 <= nums[i] <= 104

#CODE

#We are making Min Heap in this because humey largest element return krvana hai
#So min heap mei top most element sabse chota hota hai
#We will store the kth largest elements in hp

import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        hp = []          #Empty array
        for el in nums: #for element in nums 
            #len(hp) < k i.e hp mei kth element se kam element present hai
            #hp[0] < el i.e hp ka top element humara chota hai coming element se
            if len(hp) < k or hp[0] < el:
                heapq.heappush(hp,el)   #push krdo element dono cases mei
            if len(hp) > k:            #agar hp ki length badi hojaye kth element se
                heapq.heappop(hp)      #pop krdo top ka element kuki vo sabse chota hai
        return hp[0]                    #return krdo top ka element 