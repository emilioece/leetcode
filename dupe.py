def remdupe(nums:list) -> int:
    prev, count, index = nums[0], 1, 1
    print(f'nums:{nums}')
    for i in range(1, len(nums)):
        print(f'{prev} -> ({nums[i]})')
        if nums[i] == prev:
            if count < 2:
                nums[index] = nums[i]
                count +=1
                index +=1
        else:
            # reset count but i want to store it somewhere ? 
            nums[index] = nums[i]
            index +=1
            count = 1
        prev = nums[i]
    print(index)



if __name__ == '__main__':
    nums = [0,0,1,1,1,1,2,3,3]
    ans = remdupe(nums)
    # print(f'temp nums = {ans}\n{nums}')