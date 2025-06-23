import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

# Calculate the Euler-Mascheroni constant
gamma = mp.euler

# Compute the result: 1 minus the Euler-Mascheroni constant
result = 1 - gamma

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))