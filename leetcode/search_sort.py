from random import randint
def bubble_sort(nums):
    for n in range(len(nums)-1, 0, -1):
        for i in range(n):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
    return nums

test_array = [randint(a=0, b=100) for i in range(100)]
print(bubble_sort(test_array) == sorted(test_array))