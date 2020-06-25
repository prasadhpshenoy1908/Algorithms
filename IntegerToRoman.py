class Solution:
    string = ""
    number = 1 
    ################################################
    #
    # GenRomanNumber method is used to generate Roman Numbers 
    # Parameters: strToappend --> Roman Character to append
    #             div --> divisor (1000,900,500,....)
    # Return : doesnt return anything. It will update class member variable
    #################################################
    def GenRomanNumber (self, strToappend, div):
        if self.number/div > 0:
            for _ in range(int(self.number/div)):
                self.string = self.string + (strToappend)
            self.number = self.number%div
        
    def intToRoman(self, num: int) -> str:
        self.number = num
        self.GenRomanNumber("M",  1000)
        self.GenRomanNumber("CM",  900)
        self.GenRomanNumber("D",   500)
        self.GenRomanNumber("CD",  400)
        self.GenRomanNumber("C",   100)
        self.GenRomanNumber("XC",   90)
        self.GenRomanNumber("L",    50)
        self.GenRomanNumber("XL",   40)
        self.GenRomanNumber("X",    10)
        self.GenRomanNumber("IX",    9)
        self.GenRomanNumber("V",     5)
        self.GenRomanNumber("IV",    4)
        self.GenRomanNumber("I",     1)
        return self.string

def main():
    obj = Solution()
    print (obj.intToRoman(1994))

if __name__ == "__main__":
    main()