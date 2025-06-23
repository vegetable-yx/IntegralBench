import mpmath as mp
mp.dps = 15

# Calculate Euler-Mascheroni constant
gamma = mp.euler

# Compute 1 - gamma
result = 1 - gamma

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))