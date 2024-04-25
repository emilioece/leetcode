def rotate(nums:list, k:int) -> None:
    n = len(nums)
    # if k = 7 with n =7, 0 rotations :3
    k = k % n 

    front = nums[-k:]
    back = nums[:n-k]


    nums[:k] = front
    nums[k:] = back
    return None
if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7]
    indices = [x for x in range(7)]
    k = 3
    rotate(nums, k)
    print(nums)
    print(indices)
