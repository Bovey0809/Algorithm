from random import randint


def bubble_sort(nums):
    for n in range(len(nums) - 1, 0, -1):
        for i in range(n):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
    return nums


test_array = [randint(a=0, b=100) for i in range(100)]
print(bubble_sort(test_array) == sorted(test_array))


def insertion_sort(nums):
    for i in range(1, len(nums)):
        j = i
        while j > 0 and nums[j - 1] > nums[j]:
            nums[j], nums[j-1] = nums[j-1], nums[j]
            j -= 1
    print(nums)


random_array = [randint(0, 10) for i in range(10)]
insertion_sort(random_array)


def faster_insertion_sort(nums):
    for i in range(1, len(nums)):
        x = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > x:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = x


random_array = [randint(0, 100) for i in range(10)]
faster_insertion_sort(random_array)
print(random_array)


def shell_sort(arr):
    sublistcount = len(arr) // 2
    while sublistcount:
        for start in range(sublistcount):
            gap_insertion_sort(arr, start, sublistcount)
        sublistcount = sublistcount // 2


def gap_insertion_sort(arr, start, gap):
    for i in range(start + gap, len(arr), gap):
        currentvalue = arr[i]
        position = i
        while position >= gap and arr[position - gap] > currentvalue:
            arr[position] = arr[position - gap]
            position = position - gap
        arr[position] = currentvalue

test_array = [randint(1, 100) for i in range(10)]
shell_sort(test_array)
print(test_array)

def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        lefthalf = arr[:mid]
        righthalf = arr[mid:]
        mergesort(lefthalf)
        mergesort(righthalf)
        i = j = k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                arr[k] = lefthalf[i]
                i += 1
            else:
                arr[k] = righthalf[j]
                j += 1
            k += 1
        
        while i < len(lefthalf):
            arr[k] = lefthalf[i]
            i += 1
            k += 1
        while j < len(righthalf):
            arr[k] = righthalf[j]
            j += 1
            k += 1

test_array = [1, 13, 12, 4, 5]
mergesort(test_array)
print(test_array)
                