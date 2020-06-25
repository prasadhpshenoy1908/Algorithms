class Solution:
    def threeSum(self, nums):
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums [i] == nums[i -1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while (left < right):
                a = nums[left]
                b = nums[right]
                t = nums[i]
                if (nums[left] + nums[right] + nums[i] == 0):
                    res.append([nums[i], nums[left] , nums[right]])
                    left += 1
                    right -= 1
                    while(left < right and nums[left] == nums[left-1]):
                        left += 1
                    while(right < len(nums)-1 and left < right and nums[right] == nums[right+1]):
                        right -= 1
                elif (nums[left] + nums[right] + nums[i] < 0):
                    left += 1
                elif (nums[left] + nums[right] + nums[i] > 0):
                    right -= 1
        print (res)
        return res

def main():
    obj = Solution()
    obj.threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6])
    obj.threeSum([-1,0,1,2,-1,-4])
    obj.threeSum([0,0,0,0])
    obj.threeSum([-2,0,0,2,2])

if __name__ == "__main__":
    main()