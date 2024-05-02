def hindex(citations: list) -> int:
    h = 0 
    n = len(citations)
    citations.sort(reverse=True)

    for i in range(n):
        if citations[i] >= i+1:
            h  = i + 1
        else:
            break

    return h

    
def solve(func):
    from solve import cin, parr
    ans = []
    t = cin('int')
    for i in range(t):
        nums = cin('arr')
        ans.append(func(nums))
    parr(ans)

if __name__ == "__main__":
    solve(hindex)
