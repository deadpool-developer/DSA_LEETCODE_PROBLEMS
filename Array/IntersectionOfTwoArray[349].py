#Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and
#you may return the result in any order.

#Example 1:

#Input: nums1 = [1,2,2,1], nums2 = [2,2]
#Output: [2]
#Example 2:

#Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
#Output: [9,4]
#Explanation: [4,9] is also accepted.
 

#Constraints:

#1 <= nums1.length, nums2.length <= 1000
#0 <= nums1[i], nums2[i] <= 1000

#CODE
class Solution(object):
    def intersection(self, nums1, nums2):
        m = {}                     #make map
        if len(nums1) < len(nums2): #if len of nums1 is less than the len of nums2 
            nums1, nums2 = nums2 , nums1  #swap both of them
        for i in nums1:            
            if i not in m:         #insert the values in the map
                m[i] = 1           #if not present add them in the map
            else:
                m[i] +=1
        result = []
        for i in nums2:
            if i in m and m[i]:
                m[i] -= 1
                result.append(i)
        return set(result)