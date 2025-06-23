import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the square root of 2
sqrt2 = mp.sqrt(2)

# Compute the expression inside the logarithm: (3 + 2*sqrt2)/2
inner_expr = (3 + 2 * sqrt2) / 2

# Calculate the natural logarithm of the inner expression
log_val = mp.log(inner_expr)

# Compute the constant term: sqrt2/2
constant_term = sqrt2 / 2

# Combine all parts: log_val - 1 + constant_term
result = log_val - 1 + constant_term

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))