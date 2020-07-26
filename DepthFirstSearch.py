###############################################
#
#Binary Tree
#This covers following:
#     Insertion
#     DepthFirstSearch
#     
###############################################

class binaryTree:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left  = None

class binaryTreeOperations:
    def __init__(self):
        self.root = None
    
    #insert operation.
    def InsertNode(self, value):
        if self.root is None:
            self.root = binaryTree(value)
            return
        else:
            self._InsertNode(self.root, value)
            return
    
    def _InsertNode(self, _curNode, value):
        if _curNode.value < value:
            if _curNode.right is None:
                _curNode.right = binaryTree(value)
            else:
                self._InsertNode(_curNode.right, value)
        elif _curNode.value > value:
            if _curNode.left is None:
                _curNode.left = binaryTree(value)
            else:
                self._InsertNode(_curNode.left, value)
        else : 
            print("Value is not unique")

    