memo = {0: 0, 1: 1}

def fib(n):
    if n in memo:  # Base case
        return memo[n]

    result = fib(n - 1) + fib(n - 2)
    memo[n] = result
    return result

# Example usage
if __name__ == "__main__":
    print(fib(23))
    print(memo)