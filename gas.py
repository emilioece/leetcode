def circuit(gas:list, cost:list) -> int:
    n = len(gas)
    gas_count = cost_count = index = tank = 0
    
    for i in range(n):
        gas_count +=gas[i]
        cost_count += cost[i]
        tank += gas[i] - cost[i]
        
        if tank < 0:
            index +=1
            tank = 0
    if gas_count < cost_count:
        return -1 
    return index
def solve(func):
    from solve import cin, parr, output
    ans = []
    t = cin('int')
    for i in range(t):
        gas = cin('arr')
        cost = cin('arr')
        ans.append(func(gas, cost))
                          
    parr(ans)


if __name__ == "__main__":
    solve(circuit)
