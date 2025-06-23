import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate Euler-Mascheroni constant
gamma = mp.euler

# Compute the expression: 1 - gamma
result = 1 - gamma

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))