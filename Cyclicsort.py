def cyclic_sort_ascdening_order(nums):
  # TODO: Write your code here
  i = 0
  while i < len(nums):
    if nums[i] != (i+1) :
      temp = nums[i]
      nums[i] = nums[temp-1]
      nums[temp-1] = temp
    else:
      i+=1
  return nums

def FindMissingNumber(nums):
    i = 0
    while i < len(nums):
        j = nums[i]
        if (nums[i] < len(nums) and nums[i] != i):
            #do swapping
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    for i in range(len(nums)) :
        if nums[i] != i:
            print ( i )
            return i

def FindAllMissingNumber(nums):
    i , n = 0 , len(nums)
    res = []
    while i < n:
        j = nums[i]-1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    for i in range(n):
        if nums[i] != i+1:
            res.append(i+1)
    print (res)
    return res

def find_first_missing_positive(nums):
    i, n = 0, len(nums)

    while i < n:
        j = nums[i]-1
        if nums [i] > 0 and nums[i] < n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    
    for i in range(n):
        if nums[i] != i+1:
            print(i + 1)
            return(i+1)
    return -1

if __name__ == "__main__":
    array = [6,5,4,1,2,3]
    cyclic_sort_ascdening_order(array)

    array = [8,5,0,4,1,2,3,6]
    FindMissingNumber(array)

    array = [2, 3, 1, 8, 2, 3, 5, 1]
    FindAllMissingNumber(array)

    print(find_first_missing_positive([-3, 1, 5, 4, 2]))
    print(find_first_missing_positive([3, -2, 0, 1, 2]))
    print(find_first_missing_positive([3, 2, 5, 1]))