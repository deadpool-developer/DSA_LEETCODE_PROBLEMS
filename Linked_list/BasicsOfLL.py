class Node:
    def __init__(self,data,next=None):
        self.data= data
        self.next = next
    
# a = Node(1,None)
# b = Node(2)
# c = Node(3,None)

a = Node(1,Node(2,Node(3,None)))

# a.next = b
# b.next = c

def print__LL(a):  #prints the node
    while a:
        print(a.data)
        a = a.next
        
def count__LL(a):  #gives count of the nodes
    c = 0
    while a:
        c += 1
        a = a.next
    print(f"this LL has {c} nodes")
    
def insert_at_last(head,data):
    n = Node(data) #data that is passed to ne inserted
    if not head:   #if head is None -> No node is present
        return n   #returns the element that is inserted
    p = head       # creating a pointer p to head
    while p.next:  #until p points to NONE
        p = p.next
    p.next = n     #add the element at last
    return head    #return all the nodes
    
def insert_at_front(head,data):
    n = Node(data)
    n.next = head    #next stores the address of head
    return n         #returns the list
    
def delete_Kth(head,K):
    if K == 0:    #first index
        return head.next
    p = head
    while K > 1:
        K -= 1    
        p = p.next    #reaches at (K-1)th position
    p.next = p.next.next  #delete the node
    return head
    

    
a = insert_at_front(a,12)  
a = delete_Kth(a,3)
a = insert_at_last(a,10)   #returns all the nodes
# a = insert_at_last(None,10)  #returns 10



        
print__LL(a)
count__LL(a)