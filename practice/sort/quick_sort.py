class Solution:
    def quick_sort(self, left, right, nums):
        if left >= right:
            return
        temp_idx = self.partitions(left, right, nums)
        self.quick_sort(left, temp_idx - 1, nums)
        self.quick_sort(temp_idx + 1, right, nums)

    @staticmethod
    def partitions(left, right, nums):
        temp = nums[left]
        while left < right:
            while left < right and nums[right] >= temp:
                right -= 1
            nums[left] = nums[right]

            while left < right and nums[left] <= temp:
                left += 1
            nums[right] = nums[left]

        nums[left] = temp
        return left


if __name__ == '__main__':
    nums = [1, 3, 7, 5, 2, 6]
    Solution().quick_sort(0, len(nums)-1, nums)
    print(nums)