#Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

#Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

#Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.


#Example 1:


#Input: root = [1, 2, 3, null, null, 4, 5]
#Output: [1, 2, 3, null, null, 4, 5]
#Example 2:

#Input: root = []
#Output: []


#Constraints:

#The number of nodes in the tree is in the range[0, 104].
#-1000 <= Node.val <= 1000

#CODE
class TreeNode():
    pass

class Codec:
    def serialize(self, root):
        if root:
            return str(root.val) + "(" + self.serialize(root.left) + ")(" + self.serialize(root.right) + ")"
        return "X"
        
    def deserialize(self, data):
        if data == "X":
            return None
        data = data.split("(",1)
        n = TreeNode(int(data[0]))
        count = 1
        data = data[1]
        for i in range(len(data)):
            c = data[i]
            if c == "(":
                count +=1
            elif c == ")":
                count -= 1
                if count == 0:
                    n.left , n.right = self.deserialize(data[:i]) , self.deserialize(data[i+2:-1])
                    return n