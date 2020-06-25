import math
class CommonPrefix:
    def __init__(self):
        super().__init__()
        #initialize shortest string
        #This will contain shortest string in the array
        self.shorteststr = ""
    
    def _getshorteststring(self, strs):
        #Temporary assing to first element in array
        self.shorteststr= strs[0]
        #loop through the array to find the shortest element
        for str in strs:
            if len(self.shorteststr) > len (str):
                self.shorteststr = str
    
    #Binary search approach to find the common prefix
    def _UseBinarySearch(self, strs):
        left  = 0
        mid = 0
        right = len(self.shorteststr)
        while left<=right:
            #Using ceil as typecasting to int sometimes doesnt retrun appropriate data
            #sometime int((2+3)/2) was returing 2 instead of 3. This would result in skipping one character
            mid = math.ceil((left + right)/2)
            #below if else condition checks if first n characters are present in all elements
            #if it present left is increments to check n+1 characters. 
            #if its not present it right will decrement resulting in checking of n-1 characters
            if(self._contains(strs, mid)):
                left = left + 1
            else:
                right = right - 1
        return(self.shorteststr[0:mid])
    
    def _contains(self, strs, ilen):
        for str in strs:
            if self.shorteststr[:ilen] != str[:ilen]:
                return False
        return True

    def GetCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        self._getshorteststring(strs)
        return(self._UseBinarySearch(strs))


def main():
    obj = CommonPrefix()
    str = obj.GetCommonPrefix(["fleet","flex","flexing"])
    print(str)
    str = obj.GetCommonPrefix(["dog","car"])
    print(str)
    str = obj.GetCommonPrefix(["",""])
    print(str)
    str = obj.GetCommonPrefix(["dog"])
    print(str)
    str = obj.GetCommonPrefix([])
    print(str)

if __name__ == "__main__":
    main()