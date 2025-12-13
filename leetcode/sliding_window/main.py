def maxProfit(prices):
    l, r = 0, 1 # left=buy right=sell
    maxP = 0

    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxP = max(maxP, profit)
        else:
            l = r
        r += 1
    return maxP




if __name__ == "__main__":
    # buy time to buy and sell stock test cases for sliding window  
    # Test cases
    prices1 = [7, 1, 5, 3, 6, 4]
    prices2 = [7, 6, 4, 3, 1]
    print(maxProfit(prices1))  # Output: 5
    print(maxProfit(prices2))  # Output: 0