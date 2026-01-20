

# def max (nums):
#     max_num=nums[0]
#     for num in nums:
#         if num>max_num:max_num=num
#     return max_num 
# nums=[1,2,3,4,5]
# print(max(nums))
# value base
def find_max(nums):
    if not nums:
        raise ValueError("The input list cannot be None or empty.")
    max_num=nums[0]
    for i,num in enumerate(nums):
        if num>max_num:
            max_num=num
    return max_num
# index base
def max_nums(nums):
    if not nums:
        raise ValueError("The input list cannot be None or empty.")
    max_nums=nums[0]
    for i in range(1,len(nums)):
        if nums[i]>max_nums:
            max_nums=nums[i]
            
    return max_nums