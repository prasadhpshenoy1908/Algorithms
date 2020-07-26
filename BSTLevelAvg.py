from collections import deque

class binaryTee:
    def __init__(self,data = None):
        self.value = data
        self.right = None
        self.left = None

class bstOpt:
    def __init__(self):
        self.root = None

    def Insert (self, value):
        if self.root is None:
            self.root = binaryTee(value)
        else :
            self._InsertNode(self.root,value)
    
    def _InsertNode(self,Node,value):
        if Node.value > value:
            if Node.left is None:
                Node.left = binaryTee(value)
            else:
                self._InsertNode(Node.left,value)
        else:
            if Node.right is None:
                Node.right = binaryTee(value)
            else:
                self._InsertNode(Node.right,value)
    
    def InorderTraversal(self):
        if self.root is not None:
            self._InOrderTraversal(self.root)
    
    def _InOrderTraversal(self, Node):
        if Node is not None:
            self._InOrderTraversal(Node.left)
            print (Node.value)
            self._InOrderTraversal(Node.right)

    def PreorderTraversal(self):
        if self.root is not None:
            self._PreOrderTraversal(self.root)
    
    def _PreOrderTraversal(self, Node):
        if Node is not None:
            print (Node.value)
            self._PreOrderTraversal(Node.left)
            self._PreOrderTraversal(Node.right)

    def PostorderTraversal(self):
        if self.root is not None:
            self._PostorderTraversal(self.root)
    
    def _PostorderTraversal(self, Node):
        if Node is not None:
            self._PostorderTraversal(Node.left)
            self._PostorderTraversal(Node.right)
            print (Node.value)

    def levelAvg(self):
        if self.root is None:
            return 0

        queue = deque()
        queue.append(self.root)
        result = []

        while(queue):
            iLen = len(queue)
            #curNodeList = [] 
            i = 0
            sum = 0
            for i in range(iLen):
                curNode = queue.popleft()
                #curNodeList.append(curNode.value)
                sum += curNode.value
                if curNode.right is not None:
                    queue.append(curNode.right)
                if curNode.left is not None:
                    queue.append(curNode.left)
            avg = sum / iLen
            result.append(avg)
        print (str(result))


if __name__ == "__main__":
    objbstOpt = bstOpt()

    objbstOpt.Insert(6)
    objbstOpt.Insert(3)
    objbstOpt.Insert(2)
    objbstOpt.Insert(10)
    objbstOpt.Insert(11)
    objbstOpt.Insert(4)
    objbstOpt.Insert(5)
    objbstOpt.Insert(1)
    objbstOpt.Insert(12)
    objbstOpt.Insert(17)
    objbstOpt.Insert(16)
    objbstOpt.Insert(15)

    print ("In Order Traversal")
    objbstOpt.InorderTraversal()
    print ("In PreOrder Traversal")
    objbstOpt.PreorderTraversal()
    print ("In PostOrder Traversal")
    objbstOpt.PostorderTraversal()

    objbstOpt.levelAvg()
