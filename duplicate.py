def removedupe(nums:list) -> int:
    seen = nums[0]
    index = 1

    for i in range(1, len(nums)):
        if nums[i] != seen:
            seen = nums[i]
            nums[index] = seen
            index += 1
    return index

if __name__ == '__main__':
    nums = [0,0,1,1,1,2,2,3,3,4]
    ans = removedupe(nums)
    print(nums, ans)