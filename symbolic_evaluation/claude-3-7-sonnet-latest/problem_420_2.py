import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the square root of 5
sqrt5 = mp.sqrt(5)

# Compute the common expression: (sqrt(5) - 1) / 2
common_expr = (sqrt5 - 1) / 2

# Compute the logarithm term: (1/2) * ln(common_expr)
log_term = 0.5 * mp.log(common_expr)

# Compute the entire expression: log_term + common_expr
result = log_term + common_expr

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))