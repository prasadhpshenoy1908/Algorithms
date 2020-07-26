##################################################################
#
#Linked List Operations
#    Add
#    Delete
#    InPlaceReversal
#    SplitBasedonPivot
#
###################################################################

###################################################################
#LinkedListNode
#     Value
#     NextNode
#
###################################################################
class LinkedListNode:
    def __init__(self, data = None):
        self.value = data
        self.NextNode = None

###################################################################
#
#MyLinkedList Class
#  Carries out all linkedlist operations
#
###################################################################
class MyLinkedList:
    def __init__(self):
        self.head = None
    
    #Adds value to the end of LinkedList
    def AddValue(self, value):
        if self.head == None:
            self.head = LinkedListNode(value)
        else:
            curNode = self.head
            while curNode.NextNode is not None:
                curNode = curNode.NextNode
            curNode.NextNode = LinkedListNode(value)

    #Helper function to print all the elements in Linkedlist
    def PrintAll(self):
        eList = []
        curNode = self.head
        while (curNode is not None):
            eList.append(curNode.value)
            curNode = curNode.NextNode
        print (eList)
    
    #Computes length of linked list
    def Length(self):
        iCount = 0
        curNode = self.head
        while (curNode is not None):
            iCount += 1 
            curNode = curNode.NextNode
        print("Length : ",iCount)
    
    #deletes specific element from LinkedList
    def deletevalue (self,value):
        curNode = self.head
        prevNode = self.head
        while (curNode is not None and curNode.value != value):
            prevNode = curNode
            curNode = curNode.NextNode
        if curNode == None:
            print ("ERROR : value not found")
            return
        prevNode.NextNode = curNode.NextNode

    #Split linked list based on pivot value
    def splitArray(self,value):
        before = before_head = LinkedListNode(0)
        after  = after_head  = LinkedListNode(0)
        curNode = self.head
        while curNode is not None:
            if curNode.value < value:
                before.NextNode = curNode
                before = before.NextNode
            else:
                after.NextNode = curNode
                after = after.NextNode
            curNode = curNode.NextNode
        before.NextNode = after_head.NextNode
        curNode = before_head.NextNode
        self.head = curNode
 
    #Reverse linkedlist. Does inplace reversal
    def InPlaceReversal(self):
        curNode = self.head
        preNode = None
        while curNode is not None:
            NextNode = curNode.NextNode
            curNode.NextNode = preNode
            preNode = curNode
            curNode = NextNode
        self.head = preNode         

def main():
    objLinkedList = MyLinkedList()
    objLinkedList.AddValue(60)
    objLinkedList.AddValue(20)
    objLinkedList.AddValue(10)
    objLinkedList.AddValue(30)
    objLinkedList.AddValue(15)
    objLinkedList.AddValue(25)
    objLinkedList.AddValue(80)
    objLinkedList.PrintAll()
    objLinkedList.Length()
    objLinkedList.splitArray(30)
    #objLinkedList.deletevalue(60)
    objLinkedList.PrintAll()
    objLinkedList.Length()
    objLinkedList.InPlaceReversal()
    objLinkedList.PrintAll()

if __name__ == "__main__":
    main()
