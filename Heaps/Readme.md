# PROOF OF HEAP

## FOR PERFECT HEAP

mc = n/4 + 2n/8 + 3n/16 + 4n/32 + 5n/64 + ....
 
mc = 2n(1/4 + 2/8 + 3/16 + 4/32 + 5/64 + ...)
 
=> mc/2n = 1/4 + 2/8 + 3/16 + 4/32 + 5/64 + ... : equation A
 
mc = 2n(1/4 + 1/8 + 1/16 + 1/32 + 1/64 + ...           # this equals 1/2
            + 1/8 + 2/16 + 3/32 + 4/64 + ...)
 
mc = 2n(1/2 + 1/8 + 2/16 + 3/32 + 4/64 + ...)
mc = n + 2n(1/8 + 2/16 + 3/32 + 4/64 + ...)
mc = n + 2n/2(1/4 + 2/8 + 3/16 + 4/32 + 5/64 + ...)
substitutinng from eq A
 
mc = n + n(mc/2n)
 
=> mc = 2n
 
time complexity = O(n)



## FOR NOT PERFECT HEAP

if there are n elements in a heap of k levels (starting from 0) and last level has x elements
 
we can say that 2^0 + 2^1 + 2^2 + ... + 2^(k-1) + x = n
 
=> n = 2^(k) -1 + x
=> n + 1 -x = 2^(k)
 
leaf nodes (l) = x + 2^(k-1) - (x+1)/2
l = x + 2^k/2 -x/2 -1/2
 
= x/2 -1/2 + n/2 + 1/2 - x/2
 
= n/2
 
l = n/2