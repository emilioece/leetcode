def buystock(prices:list) -> int:
    profit = 0
    bought = prices[0]

    for price in prices:
        if bought < price:
            profit+= price - bought
        bought = price
    return profit
    
if __name__ == '__main__':
    prices = [1,2,3,4,5]

    ans = buystock(prices)

    print(ans)