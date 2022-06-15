def absolute_value_sum_min(nums: List[int]) -> int:
    listSize = len(nums)
    isEven = listSize % 2 == 0

    return nums[listSize // 2 - 1] if isEven else nums[listSize // 2]

print(absolute_value_sum_min([2, 4, 7]))

def searchSortedRotatedList(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid

        # left to mid part is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid +1
            else:
                right = mid - 1
    return -1

print(searchSortedRotatedList([0,1,2,5,7,8,9])