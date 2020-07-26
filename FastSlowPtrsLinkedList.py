###################################################
#
# Fast and Slow Pointer Operations
#      Is LinkedList Cyclic
#      Cycle Length
#      Cycle Start
#      Palindrome List
#      Reorder LinkedList
######################################################
class linkedListNode:
    def __init__(self, data=None):
        self.value = data
        self.NextNode = None

class cyclicLinkedListOpt:
    @staticmethod
    def IsCyclic(head):
        slowPointer = head
        fastPointer = head
        while fastPointer is not None and fastPointer.NextNode is not None:
            fastPointer = fastPointer.NextNode.NextNode
            slowPointer = slowPointer.NextNode
            if slowPointer == fastPointer:
                return True
        return False
    
    @staticmethod
    def CycleLen(head):
        slowPointer = head
        fastPointer = head
        flag = False
        while fastPointer is not None and fastPointer.NextNode is not None:
            fastPointer = fastPointer.NextNode.NextNode
            slowPointer = slowPointer.NextNode
            if slowPointer == fastPointer:
                flag = True
                break
        if flag == False:
            return

        # Initialize newSlowPointer to SlowPointer.
        # move newslowpointer till it meets slowpointer again.
        # Number of moves made by new slowpointer gives the length 
        NewSlowPointer = slowPointer
        Len = 0
        while True:
            NewSlowPointer = NewSlowPointer.NextNode
            Len += 1
            if NewSlowPointer == slowPointer:
                return Len

    @staticmethod
    def GetCycleStartNode(head):
        Cycle_Len = cyclicLinkedListOpt.CycleLen(head)
        Pointer1 = head
        Pointer2 = head
        while Cycle_Len != 0:
            Pointer2 = Pointer2.NextNode
            Cycle_Len -= 1
        while Pointer1 is not None and Pointer2 is not None:
            if Pointer1 == Pointer2:
                return (Pointer1.value)
            Pointer1 = Pointer1.NextNode
            Pointer2 = Pointer2.NextNode
    
    @staticmethod
    def getMiddleNode(head):
        slowPtr = head
        fastPtr = head
        while fastPtr is not None and fastPtr.NextNode is not None:
            fastPtr = fastPtr.NextNode.NextNode
            slowPtr = slowPtr.NextNode
        #print ("Middle Value is : ",slowPtr)
        return slowPtr

    @staticmethod
    def reverse(head):
        curNode = head
        prevNode = None
        while curNode is not None:
            NextNode = curNode.NextNode
            curNode.NextNode = prevNode
            prevNode = curNode
            curNode = NextNode
        elements=[]
        curNode = prevNode
        while curNode is not None:
            elements.append(curNode.value)
            curNode = curNode.NextNode
        #print ("reversed List : ",elements)
        return prevNode

    @staticmethod
    def CheckPalindrome(head):
        curNode = head
        MiddleNode = cyclicLinkedListOpt.getMiddleNode(curNode)
        revList = cyclicLinkedListOpt.reverse(MiddleNode)
        copy_revList = revList
        bFlag = True
        while curNode is not None and revList is not None:
            if curNode.value != revList.value:
                bFlag = False
                break
            curNode = curNode.NextNode
            revList = revList.NextNode
        cyclicLinkedListOpt.reverse(copy_revList)
        if bFlag == True:
            return True
        return False

    @staticmethod
    def reOrderList(head):
        curNode = head
        MiddleNode = cyclicLinkedListOpt.getMiddleNode(curNode)
        revList = cyclicLinkedListOpt.reverse(MiddleNode)
        while head is not None and revList is not None:
            temp = head.NextNode
            head.NextNode = revList
            head = temp

            temp = revList.NextNode
            revList.NextNode = head
            revList= temp
        if head.NextNode is not None:
            head.NextNode = None

        elements=[]
        while curNode is not None:
            elements.append(curNode.value)
            curNode = curNode.NextNode
        print ("Array Elements : ",elements)


def main():
    head = linkedListNode(10)
    head.NextNode = linkedListNode(20)
    head.NextNode.NextNode = linkedListNode(30)
    head.NextNode.NextNode.NextNode = linkedListNode(40)
    head.NextNode.NextNode.NextNode.NextNode = linkedListNode(50)
    print ("Is Cyclic ? ",cyclicLinkedListOpt.IsCyclic(head))

    CyclicNode = linkedListNode(10)
    CyclicNode.NextNode = linkedListNode(20)
    CyclicNode.NextNode.NextNode = linkedListNode(30)
    CyclicNode.NextNode.NextNode.NextNode = linkedListNode(40)
    CyclicNode.NextNode.NextNode.NextNode.NextNode = CyclicNode.NextNode.NextNode
    print ("Is Cyclic ? ",cyclicLinkedListOpt.IsCyclic(CyclicNode))
    print ("Cycle Len : ",cyclicLinkedListOpt.CycleLen(CyclicNode))
    print ("Cycle Start is : ",cyclicLinkedListOpt.GetCycleStartNode(CyclicNode))

    CyclicNode.NextNode.NextNode.NextNode.NextNode = CyclicNode
    print ("Cycle Len ? ",cyclicLinkedListOpt.CycleLen(CyclicNode))
    print ("Cycle Start is : ",cyclicLinkedListOpt.GetCycleStartNode(CyclicNode))

    PalNode = linkedListNode(10)
    PalNode.NextNode = linkedListNode(20)
    PalNode.NextNode.NextNode = linkedListNode(30)
    PalNode.NextNode.NextNode.NextNode = linkedListNode(40)
    PalNode.NextNode.NextNode.NextNode.NextNode = linkedListNode(30)
    PalNode.NextNode.NextNode.NextNode.NextNode.NextNode = linkedListNode(20)
    PalNode.NextNode.NextNode.NextNode.NextNode.NextNode.NextNode = linkedListNode(10)
    print ("Is List Palindrome : ",cyclicLinkedListOpt.CheckPalindrome(PalNode))

    ReOrderNode = linkedListNode(10)
    ReOrderNode.NextNode = linkedListNode(20)
    ReOrderNode.NextNode.NextNode = linkedListNode(30)
    ReOrderNode.NextNode.NextNode.NextNode = linkedListNode(40)
    ReOrderNode.NextNode.NextNode.NextNode.NextNode = linkedListNode(30)
    ReOrderNode.NextNode.NextNode.NextNode.NextNode.NextNode = linkedListNode(20)
    cyclicLinkedListOpt.reOrderList(ReOrderNode)

if __name__ == "__main__":
    main()
