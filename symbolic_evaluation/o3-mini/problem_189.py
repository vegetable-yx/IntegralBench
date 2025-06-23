import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Compute the square root of 2
sqrt2 = mp.sqrt(2)

# Calculate 1 + sqrt(2)
inner_expr = 1 + sqrt2

# Compute the natural logarithm of (1 + sqrt(2))
log_val = mp.log(inner_expr)

# Multiply by pi/4 to get the final result
result = (mp.pi / 4) * log_val

# Print the result rounded to 10 decimal places
print(mp.nstr(result, n=10))