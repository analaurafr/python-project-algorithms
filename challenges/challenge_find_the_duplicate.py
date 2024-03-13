def find_duplicate(nums):
    if not nums or not isinstance(nums, list) or len(nums) < 2:
        return False

    nums.sort()

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return nums[i]

    return False
