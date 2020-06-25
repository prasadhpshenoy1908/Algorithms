###############################################
#
#Binary Tree
#This covers following:
#     Insertion
#     Deletion
#     Printing
#     
###############################################

class binaryTree:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left  = None

class bTreeOperations:
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

    #delete operation.
    def deleteNode(self,value):
        if self.root is None:
            return 
        else:
            self._deleteNode (self.root , value)
            return
        
    def _deleteNode(self, _curNode, value):
        parentNode = None
        root = _curNode
        
        while _curNode is not None and _curNode.value != value:
            parentNode = _curNode

            if _curNode.value < value:
                _curNode = _curNode.right
            elif _curNode.value > value:
                _curNode = _curNode.left
        
        if _curNode is None:
            return root

        if _curNode.left is None and _curNode.right is None:
            if parentNode is None:
                self.root = None 
            elif parentNode.left == _curNode:
                parentNode.left = None
            elif parentNode.right == _curNode:
                parentNode.right = None
        
        elif _curNode.left is not None and  _curNode.right is not None:
            successorNode = self.GetNextKey(_curNode)
            self._deleteNode(root,successorNode.value)
            _curNode.value = successorNode.value
        
        else:
            if _curNode.left is not None:
                parentNode.left = _curNode.left
            elif _curNode.right is not None:
                parentNode.right = _curNode.right
        
    def GetNextKey(self,_curNode):
        _Node = _curNode.right
        while _Node.left is not None:
            _Node = _Node.left
        return _Node

    # Print Operation
    # This is also called inorder traversal
    def Asc_printNode(self):
        if self.root is None:
            print ("No values to print")
            return
        else:
            self._Asc_printNode(self.root)

    def _Asc_printNode(self,_curNode):
        if _curNode is not None:
            self._Asc_printNode(_curNode.left)
            print (str(_curNode.value))
            self._Asc_printNode(_curNode.right)

    def Desc_printNode(self):
        if self.root is None:
            print ("No values to print")
            return
        else:
            self._Desc_printNode(self.root)

    def _Desc_printNode(self,_curNode):
        if _curNode is not None:
            self._Desc_printNode(_curNode.right)
            print (str(_curNode.value))
            self._Desc_printNode(_curNode.left)


def main():
    obTOpt = bTreeOperations()
    obTOpt.InsertNode(10)
    obTOpt.InsertNode(3)
    obTOpt.InsertNode(12)
    obTOpt.InsertNode(2)
    obTOpt.InsertNode(6)
    obTOpt.InsertNode(5)
    obTOpt.InsertNode(7)
    obTOpt.InsertNode(4)
    obTOpt.InsertNode(12)
    obTOpt.InsertNode(13)
    obTOpt.InsertNode(11)

    obTOpt.Asc_printNode()
    obTOpt.deleteNode(3)
    obTOpt.Asc_printNode()



if __name__ == "__main__":
    main()