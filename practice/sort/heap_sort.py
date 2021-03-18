class Solution:
    def heapify(self, nums, i, size):
        left, right = 2 * i + 1, 2 * i + 2
        largest = i
        if left < size and nums[left] > nums[largest]:
            largest = left
        if right < size and nums[right] > nums[largest]:
            largest = right

        if largest != i:
            nums[i], nums[largest] = nums[largest], nums[i]
            self.heapify(nums, largest, size)

    def build_heap(self, nums, k):
        # 从最后一个非叶子节点开始堆化
        for i in range(k // 2 - 1, -1, -1):
            self.heapify(nums, i, k)

    def getLeastNumbers(self, arr, k: int):
        if not arr or k <= 0:
            return []
        if len(arr) <= k:
            return arr

        heap = arr[:k]
        self.build_heap(heap, k)

        for i in range(k, len(arr)):
            if arr[i] < heap[0]:
                heap[0] = arr[i]
                self.heapify(heap, 0, k)
        return heap

    def heapSort(self, arr):
        n = len(arr)
        Solution().build_heap(arr, n)
        # 一个个交换元素
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]  # 交换
            self.heapify(arr, 0, i)


if __name__ == "__main__":
    arr = [3, 2, 1]
    Solution().heapSort(arr)
    print(arr)
    print(Solution().getLeastNumbers(arr, 2))
