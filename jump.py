def canjump(nums:list) -> bool:
    max_jump = 0
    n = len(nums)

    for i in range(n):
        if i > max_jump:
            return False

        max_jump = max(max_jump, i + nums[i])

        if max_jump >= n-1:
            return True
    return False


if __name__ == "__main__":
    nums = [3,2,1,0,4]
    ans = canjump(nums)

    print(ans)