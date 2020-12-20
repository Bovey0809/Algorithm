import numpy as np
from numpy.core.fromnumeric import sort
# find the kth element in the array.


def fine_k_element(nums1, nums2, k):
    # base case
    # empty
    if not nums1:
        return nums1[-1]
    if not nums2:
        return nums2[-1]
    # k // 2  is larger than the size of the array
    if k // 2 > len(nums2) or k // 2 > len(nums1):


numbers = [i for i in range(25)]

nums1 = np.random.choice(numbers, 10)
nums2 = np.random.choice(numbers, 5)

nums2 = sort(nums2)
nums1 = sort(nums1)
print(nums1, nums2)
