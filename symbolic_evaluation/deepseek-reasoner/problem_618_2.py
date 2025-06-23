import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate Euler-Mascheroni constant
euler_mascheroni = mp.euler

# Compute the final result: 1 - γ
result = 1 - euler_mascheroni

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))