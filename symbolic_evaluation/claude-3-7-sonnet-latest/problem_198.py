import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute cosine of 1.0 radians
cos_val = mp.cos(1.0)

# Multiply by 4.0
product = 4.0 * cos_val

# Subtract from 4.0 to get final result
result = 4.0 - product

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))