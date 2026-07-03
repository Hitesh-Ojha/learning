def maxProfit(prices):
    smallest = prices[0]
    profit = 0

    for price in prices:
        if price < smallest:
            smallest = price
        else:
            profit = max(profit, price - smallest)

    return profit         

print(maxProfit([7,1,5,3,6,4]))