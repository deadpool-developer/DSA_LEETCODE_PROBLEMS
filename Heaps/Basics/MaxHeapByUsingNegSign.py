import heapq

arr = [1,4,2,3,6,8,5]

hp = []

for el in arr :
    heapq.heappush(hp, -el)
print(hp)      #this prints the min heap as we have converted the values into negative
print([-x for x in hp])  #This coverts the min heap into max heap


#Another function that converts the heap  into the max heap

heapq._heapify_max(arr)
print(arr)