import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate e squared
e_squared = mp.exp(2)

# Calculate numerator (e^2 + 1)
numerator = e_squared + 1

# Compute final result by dividing numerator by 4
result = numerator / 4

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))