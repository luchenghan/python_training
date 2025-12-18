def maxProduct(nums) -> int:
    rest = max(nums)
    curMin, curMax = 1, 1

    for n in nums:
        if n == 0:
            curMin, curMax = 1, 1
            continue

        temp = curMax * n
        curMax = max(n * curMax, n * curMin, n)
        curMin = min(temp, n * curMin, n)

        rest = max(rest, curMax)
    return rest

if __name__ == "__main__":
    nums = [2, 3, -2, 4]
    print(maxProduct(nums))  # Output: 6