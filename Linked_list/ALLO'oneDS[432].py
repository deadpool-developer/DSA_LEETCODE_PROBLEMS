#Design a data structure to store the strings' count with the ability to return the strings with minimum and maximum counts.

#Implement the AllOne class:

#AllOne() Initializes the object of the data structure.
#inc(String key) Increments the count of the string key by 1. If key does not exist in the data structure, insert it with count 1.
#dec(String key) Decrements the count of the string key by 1. If the count of key is 0 after the decrement, remove it from the data structure. It is guaranteed that key exists in the data structure before the decrement.
#getMaxKey() Returns one of the keys with the maximal count. If no element exists, return an empty string "".
#getMinKey() Returns one of the keys with the minimum count. If no element exists, return an empty string "".
 

#Example 1:

#Input
#["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey", "getMinKey"]
#[[], ["hello"], ["hello"], [], [], ["leet"], [], []]
#Output
#[null, null, null, "hello", "hello", null, "hello", "leet"]

#Explanation
#AllOne allOne = new AllOne();
#allOne.inc("hello");
#allOne.inc("hello");
#allOne.getMaxKey(); // return "hello"
#allOne.getMinKey(); // return "hello"
#allOne.inc("leet");
#allOne.getMaxKey(); // return "hello"
#allOne.getMinKey(); // return "leet"
 

#Constraints:

#1 <= key.length <= 10
#key consists of lowercase English letters.
#It is guaranteed that for each call to dec, key is existing in the data structure.
#At most 5 * 104 calls will be made to inc, dec, getMaxKey, and getMinKey.

#CODE

class DLL():
    def __init__(self,val,key):
        self.val = val
        self.key = key
        self.left = self.right = None
        
def delete(node):
    node.right.left, node.left.right = node.left , node.right

def insertxleftofy(x,y):
    x.left , x.right = y.left, y
    y.left  = x.left.right = x

class AllOne(object):

    def __init__(self):
        self.m = dict()  #map is created
        self.leftend, self.rightend = DLL(-1, "") , DLL(100000, "")  #leftend & rightend contain empty key and value as given in ques.
        self.leftend.right , self.rightend.left = self.rightend, self.leftend #pointing leftend and rightend to each other
        

    def inc(self, key):  #increment of the key value
        if key not in self.m:  #if key is not present in the map
            node = DLL(1,key)  #add the key with value 1
            insertxleftofy(node,self.leftend.right)  #insert the node at right of leftend
            self.m[key] = node  #insert the key value in the map
        else:
            node = self.m[key]  #if present then store it in the node
            node.val += 1  #increment it by 1
            if node.val > node.right.val:  #if node value become greater than its right node value
                n = node.right #store the right of the node in n
                delete(node)  #delete the node  
                while n.val < node.val:   #while node value is greater than the node in the right of it
                    n = n.right  #shift unyill the n.val become equal or greater
                insertxleftofy(node,n)  #insert it before that node
        

    def dec(self, key):   #decrement of the key
        node = self.m[key]  #store the key in the node
        if node.val == 1:   #if node.val is 1
            delete(node)  #delete that node
            del self.m[key]  #delete that node from the map also
        else:
            node.val -= 1  #if key has <1 value decrement it by 1
            if node.val < node.left.val:  #if the node value is less than the left of its node
                n = node.left  #store left of that node in the n
                delete(node)   #delete that node from the list
                while n.val > node.val:  #while left node are greater than the node which is decremented
                    n = n.left  #shift n to its left
                insertxleftofy(node,n.right)  #insert the node to its right of the node where the pointer is placed
        

    def getMaxKey(self):
        return self.rightend.left.key   #return the value left to the rightend
        

    def getMinKey(self):  
        return self.leftend.right.key  #return the value right to the leftend