import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate Euler-Mascheroni constant
gamma = mp.euler

# Compute the final result: 1 - gamma
result = 1 - gamma

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))