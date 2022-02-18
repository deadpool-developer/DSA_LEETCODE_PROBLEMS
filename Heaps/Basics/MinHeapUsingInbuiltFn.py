
import heapq

#Using the heapify function
arr = [1,4,2,3,6,8,5]

heapq.heapify(arr)
print(arr)


#USing the heappush function

hp = []
for el in arr:
    heapq.heappush(hp,el)
print(hp)


