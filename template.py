def solve(func):
    from solve import cin, parr
    ans = []
    t = cin('int')
    for i in range(t):
        nums = cin('arr')
        ans.append(func(nums))
    parr(ans)

if __name__ == "__main__":
    pass
