import mpmath as mp

# Set decimal places for internal precision
mp.dps = 15

# Calculate the square root of 2
sqrt2 = mp.sqrt(2)

# Compute the expression inside the logarithm: 1 + sqrt(2)
inner_expr = 1 + sqrt2

# Calculate the natural logarithm of (1 + sqrt(2))
log_val = mp.log(inner_expr)

# Multiply by pi to get the final result
result = mp.pi * log_val

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))