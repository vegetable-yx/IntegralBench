import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute arcsin(1/3)
arcsin_val = mp.asin(1/3)

# Multiply the result by pi
result = mp.pi * arcsin_val

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))