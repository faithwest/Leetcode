def matrixChainOrder(p):
    n = len(p) - 1  # Number of matrices
    
    # Create a DP table to store the minimum multiplication costs
    dp = [[0 for _ in range(n)] for _ in range(n)]
    
    # L is the chain length (number of matrices being multiplied)
    for L in range(2, n + 1):  # Start from multiplying two matrices
        for i in range(n - L + 1):
            j = i + L - 1
            dp[i][j] = float('inf')  # Initialize with a large number
            
            # Try all possible places to split the chain
            for k in range(i, j):
                q = dp[i][k] + dp[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                
                if q < dp[i][j]:
                    dp[i][j] = q
    
    return dp[0][n - 1]

# Example Usage
p = [40, 20, 30, 10, 30]
result = matrixChainOrder(p)
print(f"Minimum number of multiplications: {result}")
