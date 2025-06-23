import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate denominator component: 3 * sqrt(3)
denominator = 3 * mp.sqrt(3)

# Calculate numerator component: 2 * pi
numerator = 2 * mp.pi

# Compute final result by dividing numerator by denominator
result = numerator / denominator

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))