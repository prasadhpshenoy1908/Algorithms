###############################################
#
#Breadth First Search
#This covers following:
#     Traversing Top to bottom
#     Traversing bottom to top
#     Zigzag traversal
#     Height of tree
#     steps between 2 elements
#
###############################################
from collections import deque

class bTreeNode:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None

class bTreeOperation:
    ### Initialization
    def __init__(self):
        self.root = None
        self.depth = 0

    ### Insertion
    def InsertNode(self,value):
        if self.root == None:
            self.root = bTreeNode(value)
        else:
            self._InsertNode(self.root,value)
    
    ### Private Insert function.
    def _InsertNode(self, Node, value):
        if Node.value < value:
            if Node.right is not None:
                self._InsertNode(Node.right,value)
            else:
                Node.right = bTreeNode(value)
        elif Node.value > value:
            if Node.left is not None:
                self._InsertNode(Node.left,value)
            else:
                Node.left = bTreeNode(value)
        else:
            print("Number is present in tree")

    ### Tree traversal (Breadth First search)
    ### Print from top to bottom
    def print_TopToBottom(self):
        result = []

        if self.root is None:
            return result
        
        ### Use deque so that you can read from both sides of queue
        queue = deque()
        queue.append(self.root)

        while(queue):
            iLenSize = len(queue)
            curNodeList = []
            for _ in range (iLenSize):
                curNode = queue.popleft()

                if curNode.left:
                    queue.append(curNode.left)
                if curNode.right:
                    queue.append(curNode.right)

                curNodeList.append(curNode.value)

            result.append(list(curNodeList))
        print (str(result))

    ### Print from bottom to top
    def print_BottomToTop(self):
        result = deque()

        if self.root is None:
            return result
        
        ### Use deque so that you can read from both sides of queue
        queue = deque()
        queue.append(self.root)

        while(queue):
            iLenSize = len(queue)
            curNodeList = []
            for _ in range (iLenSize):
                curNode = queue.popleft()

                if curNode.left:
                    queue.append(curNode.left)
                if curNode.right:
                    queue.append(curNode.right)

                curNodeList.append(curNode.value)

            result.appendleft(list(curNodeList))
        print (str(result))    

    #Print in Zigzag format
    def PrintZigZag(self):
        result = []

        if self.root is None:
            return result
        
        ### Use deque so that you can read from both sides of queue
        queue = deque()
        queue.append(self.root)
        lRightToLeft = 0
        while(queue):
            iLenSize = len(queue)
            curNodeList = deque()
            for _ in range (iLenSize):
                curNode = queue.popleft()

                if curNode.left:
                    queue.append(curNode.left)
                if curNode.right:
                    queue.append(curNode.right)

                if lRightToLeft == 0:
                    curNodeList.append(curNode.value)
                else:
                    curNodeList.appendleft(curNode.value)
            lRightToLeft = not lRightToLeft
            result.append(curNodeList)
        print (str(result))
    
    #Minimun height of tree
    def Minheight(self):
        minHeigh = 0
        breakloop = False
        if self.root is None:
            minHeigh = 0
        queue = deque()
        queue.append(self.root)
        while (queue is not None):
            minHeigh = minHeigh + 1
            iLen = len(queue)
            for _ in range(iLen):
                curNode = queue.popleft()
                if (curNode.right is None and curNode.left is None):
                    breakloop = True
                    break
                if curNode.left:
                    queue.append(curNode.left)
                if curNode.right:
                    queue.append(curNode.right)
            if breakloop == True:
                break

        print ("Minimum height is : ",minHeigh)

    #depth of specific element
    def _getElementsDepth(self, sum, bstNode, Element):
        if bstNode is None:
            return -1
        if bstNode.value == Element:
            self.depth += 1
            return self.depth
        elif bstNode.value < Element:
            self.depth += 1 
            return (self._getElementsDepth(sum,bstNode.right,Element))
        else:
            self.depth += 1
            return (self._getElementsDepth(sum,bstNode.left,Element))
        return -1
            

    def getDistance(self, Element1, Element2):
        self.depth = 0
        depth1 = self._getElementsDepth(sum, self.root, Element1)
        if depth1 == -1:
            return ("Number not present")
        self.depth = 0
        depth2 = self._getElementsDepth(sum, self.root, Element2)
        if depth2 == -1:
            return ("Number not present")
        return ("Distance is ",(depth1 - depth2) + 1)

def main():
    bTreeOpt = bTreeOperation()

    bTreeOpt.InsertNode(10)
    bTreeOpt.InsertNode(4)
    bTreeOpt.InsertNode(3)
    bTreeOpt.InsertNode(2)
    bTreeOpt.InsertNode(6)
    bTreeOpt.InsertNode(5)
    bTreeOpt.InsertNode(7)
    bTreeOpt.InsertNode(8)
    bTreeOpt.InsertNode(14)
    bTreeOpt.InsertNode(13)
    bTreeOpt.InsertNode(12)
    bTreeOpt.InsertNode(11)
    
    print (bTreeOpt.getDistance(2,6))

    bTreeOpt.print_TopToBottom()
    bTreeOpt.print_BottomToTop()
    bTreeOpt.PrintZigZag()
    bTreeOpt.Minheight()

if __name__ == "__main__":
    main()
