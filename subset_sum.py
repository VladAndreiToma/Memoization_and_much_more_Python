def count_subsets(arr, target_sum):
    def backtrack(index, current_sum):
        if index == len(arr):   # Check if we looked over the whole array
            if current_sum == target_sum:  # Check if the subset has the desired sum
                return 1        # Valid
            else:
                return 0        # Not valid

        # Include the current element in the subset
        include_count = backtrack(index + 1, current_sum + arr[index])
        # Exclude the current element from the subset
        exclude_count = backtrack(index + 1, current_sum)
        # Return the combination of the two
        return include_count + exclude_count

    return backtrack(0, 0)

# Example usage
if __name__ == "__main__":
    print(count_subsets([1, 2, 3, 3], 6))