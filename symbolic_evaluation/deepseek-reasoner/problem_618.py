import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate Euler-Mascheroni constant using mpmath
euler_mascheroni = mp.euler

# Compute the final result: 1 - γ
result = 1 - euler_mascheroni

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))