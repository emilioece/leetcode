def maxprofit(prices):
    min_price = prices[0]
    max_profit = 0
    
    for price in prices:
        if price < min_price:
            min_price = price

        elif price - min_price > max_profit:
            max_profit = price - min_price
    
    return max_profit


# for this problem, you want to find the profit using the indices of the list as the days that you purchase them and you want 
# to maximize your profit, that is, you purchase for a lower price and sell at a higher price. so in this look 

# we iterate through prices in prices and if the price is less than min price (which we intialize as the first element in the list)
# then we make it the new minimum price 

# then we take the difference between price and min price and see if its graeter than max prof

# since max prof is set to 0, that means that any negative numbers are filtered out where we lose money, therefore, 
# if no profit is to be made, then profit remains at 0

# else, store the max profit in the value (given by the difference to calculate the profit :3)
