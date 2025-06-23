import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate arcsin(1/3)
arcsin_val = mp.asin(1/3)

# Multiply by pi to get the final result
result = mp.pi * arcsin_val

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))