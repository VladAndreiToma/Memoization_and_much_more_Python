#1. An exercise for bit masking concept
# Count from a given set , which subsets will have a given sum if you sum up the elements of the subset
'''
def count_subsets(arr, target_sum):
    def backtrack(index, current_sum):
        if index == len(arr):   # here is to check that we looked over the whole array
            if current_sum == target_sum:  # here it is to check if the subset has the desired sum
                return 1        # valid
            else:
                return 0        # not valid

        # Include the current element in the subset  --- goes on calling backtrack as long as in the current subset the element was not visited
        include_count = backtrack(index + 1, current_sum + arr[index])
        # Exclude the current element from the subset --- frees the stack to generate another subset
        exclude_count = backtrack(index + 1, current_sum)
        # returns the combination of the two
        return include_count + exclude_count
    # initialize backtracking with 0 index , 0 sum
    return backtrack(0, 0)


print(count_subsets( [1, 2, 3, 3] , 6 ))
'''
'''
# Memoization of Fibonnaci s string
memo = {0: 0, 1: 1}
def fib(n):
    # Base case: if n is in memo, return the cached result
    if n in memo:
        return memo[n]

    # Calculate the nth Fibonacci number using memoization
    result = fib(n - 1) + fib(n - 2)

    # Store the result in the memo dictionary for future use
    memo[n] = result

    return result
print( fib(23))
print( memo )
'''
'''
# Memoization of climbing the steps
memo = {}
def count_ways(n):
    if n in memo:
        return memo[n]
    if n == 1:      # then there is only one way to climb one stair so return n itself
        return n
    ways = [0]*(n+1)  # to be n elements cause loops go over n-1 so n-1+1 is n
    ways[0] = 1      # you can climb zero steps in one way - no climbing at all
    ways[1] = 1      # you can climb 1 step in one way - climb 1 step
    # for 2 steps or more you can climb the summation of previous steps
    for i in range( 2 , n+1 ):  # from 2 steps to n steps there are n-1 + n-2 possibilities
        ways[i] = ways[i-1] + ways[i-2]
    memo.update({n:ways[n]})
    return ways[n]

print( count_ways(4) )
print( count_ways(5))
print( count_ways(4))
print( memo )
'''
'''
def longest_common_subsequence(str1, str2):
    dim1 = len(str1)
    dim2 = len(str2)
    common_maximum_matrix = [ [0]*(dim2+1) for _ in range(dim1+1) ] # +1 cause py goes until limit - 1, therefore limit is what is supposed to be
    for i in range(1,dim1+1):
        for j in range(1,dim2+1):
            if str1[i-1] == str2[j-1]:
                common_maximum_matrix[i][j] = common_maximum_matrix[i-1][j-1]+1
            else:
                common_maximum_matrix[i][j] = max( common_maximum_matrix[i-1][j] , common_maximum_matrix[i][j-1] )
    #now basically in the last cel: [dim1][dim2]
    return common_maximum_matrix[dim1][dim2]
print(longest_common_subsequence( 'AGGTAB' , 'GXTXAYB' ))
'''
'''
def knapsack(weights, values, W):
    n = len(weights)
    # Create a table to store the maximum value for each subproblem
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, W + 1):
            # If the current item's weight is less than or equal to the current capacity, consider it
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                # If the current item's weight is more than the current capacity, skip it
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]
'''
'''
def min_coin_change(coins, amount):
    # Create a table to store the minimum number of coins needed for each amount
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # Zero coins needed to make up amount 0

    for coin in coins:
        for i in range(coin, amount + 1):
            # Update dp[i] with the minimum of dp[i] and dp[i - coin] + 1
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[amount] is still float('inf'), it means the amount cannot be made up
    if dp[amount] == float('inf'):
        return -1
    else:
        return dp[amount]
print( min_coin_change( [1,5,10] , 15 ))
'''
def do_rectangles_overlap(rect1_top_left, rect1_bottom_right, rect2_top_left, rect2_bottom_right):
    x1A , y1A = rect1_top_left
    x2A , y2A = rect1_bottom_right
    x1B , y1B = rect2_top_left
    x2B , y2B = rect2_bottom_right
    print ( x1A , y1A , x2A , y2A )
    print ( x1B , y1B , x2B , y2B )
    # 8 cases of overlap ----- 8 corners over each other this treat semi inclusions for both rectangles
    # the rest of the combinations were once a corner overlaped so those
    if (y2B < y1A and x2B > x1A) or (y2B < y1A and x1B < x2B) or      


# Rect
print( do_rectangles_overlap( [0, 2] ,[2, 0] ,[1, 1] ,[-1, -1] ))