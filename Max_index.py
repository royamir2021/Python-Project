# Problem Statement
# You are given a list of integers.
# Return the index of the first occurrence of the maximum value.
def find_max_index(nums):
    if not nums:
        raise ValueError("The input list cannot be None or empty.")
    max_index=0
    for i in range(1,len(nums)):
        if nums[i]>nums[max_index]:
            max_index=i
    return max_index

nums=[1,5,8,9,1,5]
print(find_max_index(nums))