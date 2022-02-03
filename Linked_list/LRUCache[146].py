#Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

#Implement the LRUCache class:

#LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
#int get(int key) Return the value of the key if the key exists, otherwise return -1.
#void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
#The functions get and put must each run in O(1) average time complexity.

 

#Example 1:

#"LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
#[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
#Output
#[null, null, null, 1, null, -1, null, -1, 3, 4]

#Explanation
#LRUCache lRUCache = new LRUCache(2);
#lRUCache.put(1, 1); // cache is {1=1}
#lRUCache.put(2, 2); // cache is {1=1, 2=2}
#lRUCache.get(1);    // return 1
#lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
#lRUCache.get(2);    // returns -1 (not found)
#lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
#lRUCache.get(1);    // return -1 (not found)
#lRUCache.get(3);    // return 3
#lRUCache.get(4);    // return 4
 

#Constraints:

#1 <= capacity <= 3000
#0 <= key <= 104
#0 <= value <= 105
#At most 2 * 105 calls will be made to get and put.

#CODE

class DLL():   #class to insert a dummy node 
    def __init__(self,val=0,key=0):
        self.val = val
        self.key = key
        self.left = self.right = None
        
def delete(node):  #delete the node by pointing left of next node to left node and right of previous node to next node .
    node.right.left, node.left.right = node.left, node.right
    
def insertxleftofy(x,y):  #inserts the element in between the the two node
    x.left,x.right = y.left, y
    y.left = x.left.right = x
    

class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity   #capacity of the map
        self.m = dict()   #defined map m
        self.leftend , self.rightend = DLL() , DLL()  #creating dummy node at left and right end
        self.leftend.right , self.rightend.left = self.rightend, self.leftend  #making point left node to right and vice versa

    def get(self, key):   #get the key from the list 
        if key not in self.m:   #if key is not present in the map
            return -1
        #if present
        node = self.m[key]   #storing key inside the node
        delete(node)   #delete from the node from the list
        insertxleftofy(node, self.rightend)   #insert it as a Recently used node at front of the list
        return node.val        #return the value

    def put(self, key, value):  #insert the key value pair inside the map
        if key in self.m:  #if key is present in map
            node = self.m[key]  #store the key in node
            node.val = value  #if value is changed , change the value
            delete(node)  #delete node from the list
        else:
            node = DLL(value,key)    #add the key value in the list
            self.m[key] = node  #add it in the map
        insertxleftofy(node , self.rightend)  #insert the node at the first
        if len(self.m) > self.capacity:  #if length of the map > capacity
            k = self.leftend.right.key   
            delete(self.leftend.right)
            del self.m[k]