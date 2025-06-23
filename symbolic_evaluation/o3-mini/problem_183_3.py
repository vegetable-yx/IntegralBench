import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate square root of 5
sqrt5 = mp.sqrt(5)

# Compute the expression inside the logarithm: 2 + sqrt(5)
inner_expr = 2 + sqrt5

# Compute the natural logarithm of (2 + sqrt(5))
log_val = mp.log(inner_expr)

# Multiply by pi/4 to get the final result
result = (mp.pi / 4) * log_val

# Print the result rounded to 10 decimal places
print(mp.nstr(result, n=10))