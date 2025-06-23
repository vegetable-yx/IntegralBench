import mpmath as mp

# Set internal decimal places for computation
mp.dps = 15

# Compute the square root of 2
sqrt2 = mp.sqrt(2)

# Compute the expression inside the logarithm: 1 + sqrt(2)
inner_expr = 1 + sqrt2

# Compute the natural logarithm of (1 + sqrt(2))
log_val = mp.log(inner_expr)

# Multiply the logarithm by pi
result = mp.pi * log_val

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))