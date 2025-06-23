import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate denominator component: 4 * sqrt(2)
denominator = 4 * mp.sqrt(2)

# Compute the final result by dividing pi by the denominator
result = mp.pi / denominator

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))