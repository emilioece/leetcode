def candy(ratings:list) -> int:
    return -1 

def solve(func):
    from solve import cin, parr, output
    ans = []
    t = cin('int')
    for _ in range(t):
        nums = cin('arr')
        ans.append(func(nums))
                          
    opt = output(t, 'arr')
    parr(ans)
    print('expected output:')
    parr(opt)


if __name__ == "__main__":
    solve(candy)