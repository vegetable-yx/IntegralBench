import mpmath as mp

mp.dps = 15  # Set decimal precision for calculations

# Calculate Euler-Mascheroni constant
euler_gamma = mp.euler

# Compute final result: 1 - γ
result = 1 - euler_gamma

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))