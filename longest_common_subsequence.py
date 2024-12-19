def longest_common_subsequence(str1, str2):
    dim1 = len(str1)
    dim2 = len(str2)
    common_maximum_matrix = [[0] * (dim2 + 1) for _ in range(dim1 + 1)]

    for i in range(1, dim1 + 1):
        for j in range(1, dim2 + 1):
            if str1[i - 1] == str2[j - 1]:
                common_maximum_matrix[i][j] = common_maximum_matrix[i - 1][j - 1] + 1
            else:
                common_maximum_matrix[i][j] = max(common_maximum_matrix[i - 1][j], common_maximum_matrix[i][j - 1])

    return common_maximum_matrix[dim1][dim2]

# Example usage
if __name__ == "__main__":
    print(longest_common_subsequence('AGGTAB', 'GXTXAYB'))