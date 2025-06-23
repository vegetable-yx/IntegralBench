import mpmath as mp

# Set internal decimal precision to 15 to ensure accurate 10-digit output
mp.dps = 15

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Compute 1 + sqrt(2)
inner_expr = 1 + sqrt2

# Compute natural logarithm of (1 + sqrt(2))
log_val = mp.log(inner_expr)

# Multiply by pi to get final result
result = mp.pi * log_val

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))