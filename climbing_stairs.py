memo = {}

def count_ways(n):
    if n in memo:
        return memo[n]
    if n == 1:  # One way to climb one stair
        return n
    ways = [0] * (n + 1)  # Initialize ways array
    ways[0] = 1  # No climbing
    ways[1] = 1  # Climb 1 step
    for i in range(2, n + 1):
        ways[i] = ways[i - 1] + ways[i - 2]
    memo[n] = ways[n]
    return ways[n]

# Example usage
if __name__ == "__main__":
    print(count_ways(4))
    print(count_ways(5))
    print(count_ways(4))
    print(memo)