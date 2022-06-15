def absolute_value_sum_min(nums: List[int]) -> int:
    listSize = len(nums)
    isEven = listSize % 2 == 0

    return nums[listSize // 2 - 1] if isEven else nums[listSize // 2]
