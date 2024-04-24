def merge(nums1=None, m=None, nums2=None, n=None) -> None:
    # arrays are already sorted 
    i, j, k = m - 1, n - 1, m + n - 1

    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    return nums1

if __name__ == '__main__':
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3

    ans = [1,2,2,3,5,6]

    if merge(nums1, m, nums2, n) == ans:
        print('derp')
