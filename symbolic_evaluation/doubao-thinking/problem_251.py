import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Calculate the square root of 2
sqrt2 = mp.sqrt(2)

# Compute the expression inside the logarithm: 1 + sqrt(2)
inner_expr = 1 + sqrt2

# Calculate the natural logarithm of (1 + sqrt(2))
log_value = mp.log(inner_expr)

# Multiply the logarithm by pi
result = mp.pi * log_value

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))