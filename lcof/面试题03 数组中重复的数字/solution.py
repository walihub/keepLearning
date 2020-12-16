class Solution(object):
    def findRepeatNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            while i != nums[i]:
                if nums[i] == nums[nums[i]]:
                    return nums[i]
                else:
                    temp = nums[i]
                    nums[i] = nums[temp]
                    nums[temp] = temp
        return -1

    def findRepeatNumber2(self, nums):
        nums_map = {}
        for num in nums:
            if num in nums_map:
                return num
            else:
                nums_map[num] = 1
        return -1


if __name__ == '__main__':
    nums = [2, 3, 1, 0, 2, 5, 3]
    result = Solution().findRepeatNumber2(nums)
    print("result: ", result)
