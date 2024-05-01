def jump(nums:list) -> int:
        n = len(nums)

        reach = 0
        count = 0
        end_reach = 0

        for i in range(n-1):
            reach = max(reach, i + nums[i])
            if i == end_reach:
                count +=1
                end_reach = reach

        return count
def solve(func):
    from solve import cin
    ans = []
    t = cin('int')
    for i in range(t):
        nums = cin('arr')
        ans.append(func(nums))
    for i in range(t):
        print(f'Case #{i+1}: {ans[i]}')

if __name__ == "__main__":
    solve(jump)
