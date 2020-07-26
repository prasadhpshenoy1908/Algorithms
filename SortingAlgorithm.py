def quickSort(nums):
    if len(nums) < 2:
        return nums
    print (nums)
    quicksortAlgo(nums, 0, len(nums)-1)

def quicksortAlgo (nums, left, right):
    if left < right:
        pivot = int((right-left) / 2)
        pivotVal = nums[pivot]
        index = partition (nums,left,right,pivotVal)
        quicksortAlgo(nums, left, index-1)
        quicksortAlgo(nums,index+1,right)
    return
    

def partition(nums,left,right,pivotVal):
    while left < right:
        while nums[left] < pivotVal:
            left += 1
        while nums[right] > pivotVal:
            right -= 1
        if left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
    return left

arr = [10,30,60,40,50,25]
n = len (arr)
quickSort(arr)
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]),