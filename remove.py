def remove(nums:list, val:int):
    nums.sort()
    k = len(nums)
    while val in nums:
        nums.remove(val)
        k-=1
    return k

if __name__ == '__main__':
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    remove(nums, val)