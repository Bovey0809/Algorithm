from random import randint

random_array = [randint(0, 100) for i in range(randint(10, 20))]


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


bubble_sort(random_array)


@test
def insertion_sort(nums):
    for i in range(1, len(nums)):
        temp = nums[i]
        j = i
        while nums[j - 1] > temp:
            nums[j] = nums[j - 1]
            j -= 1
        nums[j] = temp


insertion_sort(random_array)
@test
def faster_insertion_sort(nums):
    for i in range(1, len(nums)):
        x = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > x:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = x


faster_insertion_sort(random_array)


@test
def shell_sort(nums):
    gap = len(nums) // 2
    while gap:
        for i in range(gap, len(nums), gap):
            left = i - gap
            while nums[left] > nums[left + gap]:
                nums[left + gap] = nums[left]
                left -= gap
            nums[left+gap] = nums[i]
        gap = gap // 2


shell_sort(random_array)


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


inverse_shell_sort(random_array)


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


merge_sort(random_array)
print(random_array)


def quick_sort(arr):

    quick_sort_help(arr, 0, len(arr)-1)


def quick_sort_help(arr, first, last):

    if first < last:

        splitpoint = partition(arr, first, last)

        quick_sort_help(arr, first, splitpoint-1)
        quick_sort_help(arr, splitpoint+1, last)


def partition(arr, first, last):

    pivotvalue = arr[first]

    leftmark = first+1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and arr[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while arr[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            temp = arr[leftmark]
            arr[leftmark] = arr[rightmark]
            arr[rightmark] = temp

    temp = arr[first]
    arr[first] = arr[rightmark]
    arr[rightmark] = temp

    return rightmark


quick_sort(random_array)
