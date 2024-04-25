def major(nums:list) -> int:
    count = 1
    major = nums[0]

    for i in range(1, len(nums)):
        if nums[i] == major:
            count +=1
        else:
            count -=1
            if count == 0:
                major = nums[i]
                count = 1
    return major
    

if __name__ == '__main__':
    nums =[1,3,1,1,4,1,1,5,1,1,6,2,2]
    ans = major(nums)
    print(ans)
