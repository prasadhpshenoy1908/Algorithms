import sys
def LargestContSum(nums, lenght):
    sum = 0
    maxSum = 0
    iStart, iEnd = 0, len(nums)
    i = 0
    for  i in range(iEnd):
        if(i >= lenght):
            sum -= nums[iStart]
            iStart += 1
        sum += nums[i]
        maxSum = sum if (sum>maxSum) else maxSum
    return maxSum

def GetTwoLargest(nums):
    first = -sys.maxsize - 1
    second = -sys.maxsize - 1
    for i in nums:
         if i > first:
             second = first
             first = i

         if (i > second and i != first):
             second = i
    return first, second

def sumLargestNum(nums):
    first, second = GetTwoLargest(nums)
    return (first+second)

def main():
    print ("Max sum is : ", LargestContSum([-10, 2, 3, -2, 0, 5, -15],4))
    print ("Sum of Largest : ",sumLargestNum([-10, 2, 3, -2, 0, 5, -15]))
if __name__ == "__main__":
    main()