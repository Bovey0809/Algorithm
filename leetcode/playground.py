import numpy as np
from numpy.core.fromnumeric import sort

# find the kth element in the array.


def find_k_element(nums1, nums2, k) -> float:
    # base case
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    # empty
    if not nums1:
        return nums2[k - 1]
    # too large
    t = min(k // 2, len(nums1))

    if nums1[t-1] < nums2[t-1]:
        return find_k_element(nums1[t:], nums2, k-t)
    else:
        return find_k_element(nums1, nums2[t:], k-t)


print(find_k_element(nums1=[1, 2, 8, 9, 10], nums2=[3, 5, 7], k=6))
