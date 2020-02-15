from random import randint

random_array = [randint(0, 100) for i in range(randint(3, 5))]


def test(func):
    def _f(*arg):
        func(*arg)
        print(f"After {func.__name__} : {arg}")
    return _f


@test
def bubble_sort(nums):
    length = len(nums)
    for n in range(length, 0, -1):
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]


@test
def insertion_sort(nums):
    for i in range(1, len(nums)):
        temp = nums[i]
        j = i
        while nums[j - 1] > temp:
            nums[j] = nums[j - 1]
            j -= 1
        nums[j] = temp


@test
def faster_insertion_sort(nums):
    for i in range(1, len(nums)):
        x = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > x:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = x


@test
def shell_sort(nums):
    if len(nums) <= 1:
        return nums
    gap = len(nums) // 2
    while gap:
        for start in range(gap, len(nums), gap):
            temp = nums[start]
            j = start - gap
            while j >= 0 and nums[j] > temp:
                nums[j + gap] = nums[j]
                j -= gap
            nums[j + gap] = temp
        gap = gap // 2
    return nums


shell_sort([23, 57, 12, 89])


@test
def inverse_shell_sort(nums):
    gap = len(nums) // 2
    while gap:
        for start in range(gap, len(nums), gap):
            temp = nums[start]
            j = start
            while j > 0 and temp > nums[j - gap]:
                nums[j] = nums[j - gap]
                j -= gap
            nums[j] = temp
        gap = gap // 2


def merge(left, right):
    # merge two nums
    nums = []
    while left and right:
        if left[0] > right[0]:
            nums.append(right.pop(0))
        else:
            nums.append(left.pop(0))
    if left:
        nums += left
    if right:
        nums += right
    return nums
# Recursively implementation of Merge Sort


def merge_sort(nums):
    length = len(nums)
    if length <= 1:
        return nums
    mid = length // 2
    left = nums[:mid]
    right = nums[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)


# def quick_sort(arr):

#     quick_sort_help(arr, 0, len(arr)-1)


# def quick_sort_help(arr, first, last):

#     if first < last:

#         splitpoint = partition(arr, first, last)

#         quick_sort_help(arr, first, splitpoint-1)
#         quick_sort_help(arr, splitpoint+1, last)


# def partition(arr, first, last):

#     pivotvalue = arr[first]

#     leftmark = first+1
#     rightmark = last

#     done = False
#     while not done:

#         while leftmark <= rightmark and arr[leftmark] <= pivotvalue:
#             leftmark = leftmark + 1

#         while arr[rightmark] >= pivotvalue and rightmark >= leftmark:
#             rightmark = rightmark - 1

#         if rightmark < leftmark:
#             done = True
#         else:
#             temp = arr[leftmark]
#             arr[leftmark] = arr[rightmark]
#             arr[rightmark] = temp

#     temp = arr[first]
#     arr[first] = arr[rightmark]
#     arr[rightmark] = temp

#     return rightmark


def quickSort(nums):

    _quickSort(nums, 0, len(nums)-1)


def _quickSort(nums, left, right):
    pivot = _partition(nums, left, right)
    _quickSort(nums, left, pivot)
    _quickSort(nums, pivot + 1, right)


def _partition(nums, left, right) -> int:
    pivotvalue = nums[left]
    leftMark = left
    rightMark = right
    while leftMark < rightMark:
        while leftMark < rightMark and nums[leftMark] <= pivotvalue:
            leftMark += 1
        nums[rightMark] = nums[leftMark]
        while leftMark <= rightMark and nums[rightMark] >= pivotvalue:
            rightMark -= 1
        nums[leftMark] = nums[rightMark]

    return rightMark


def quick_sort(nums, left, right):
    if left >= right:
        return
    pivot = nums[left]
    leftmark = left + 1
    rightmark = right
    while leftmark < rightmark:
        while leftmark < rightmark and nums[leftmark] <= pivot:
            leftmark += 1
        while leftmark <= rightmark and nums[rightmark] >= pivot:
            rightmark -= 1
        if leftmark < rightmark:
            nums[leftmark], nums[rightmark] = nums[rightmark], nums[leftmark]
    nums[left], nums[rightmark] = nums[rightmark], nums[left]
    quick_sort(nums, left, rightmark - 1)
    quick_sort(nums, rightmark + 1, right)


print(random_array)
quick_sort([95, 54, 18], 0,  2)
print(random_array)
print(sorted(random_array) == random_array)
