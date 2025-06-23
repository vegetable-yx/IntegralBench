import mpmath as mp
mp.dps = 15  # Set internal precision

# Calculate Euler-Mascheroni constant
gamma = mp.euler

# Compute final result
result = 1 - gamma

# Print result with 10 decimal places
print(mp.nstr(result, n=10))