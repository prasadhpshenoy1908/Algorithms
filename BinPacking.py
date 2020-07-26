import sys
class Bins:
    def __init__(self,data=None):
        self.ActSize=data
        self.RemainingSize=data 
        self.Pack = []

def FirstFitAlgorithm(nums,size):
    oBinsObj = Bins(size)
    oBinsArray = []
    oBinsArray.append(oBinsObj)
    bBinPacked = False
    for i in nums:
        bBinPacked = False
        for j in oBinsArray:
            if j.RemainingSize >= i:
                PackBin(j,i)
                bBinPacked = True
                break
        if bBinPacked == False:
            oNewBinObj = Bins(size)
            PackBin(oNewBinObj,i)
            oBinsArray.append(oNewBinObj)
    for i in oBinsArray:
        print(i.Pack)

def PackBin (oBin, binsize):
    oBin.Pack.append(binsize)
    oBin.RemainingSize -=binsize

def BestFitAlgorithm(nums,Size):
    oBinsArray = []
    oBinsArray.append(Bins(Size))
    oMinbin = Bins()
    minsize = sys.maxsize
    for i in nums:
        bBinPacked = False
        for j in oBinsArray:
            if(j.RemainingSize >= i ):
                if j.RemainingSize < minsize :
                    oMinbin = j
                    bBinPacked = True
        if bBinPacked == False:
            oNewBinObj = Bins(Size)
            PackBin(oNewBinObj,i)
            oBinsArray.append(oNewBinObj)
        else:
            PackBin(oMinbin,i)
    for i in oBinsArray :
        print(i.Pack)
    

def main():
    FirstFitAlgorithm([11,2,15,5,6,17,7],20)
    FirstFitAlgorithm([2, 5, 4, 7, 1, 3, 8],10)
    BestFitAlgorithm([11,2,15,5,6,17,7],20)
    BestFitAlgorithm([2, 5, 4, 7, 1, 3, 8],10)

main()