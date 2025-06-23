import mpmath as mp

# Set internal decimal places to 15 for sufficient precision
mp.dps = 15

# Calculate the square root of 2
sqrt2 = mp.sqrt(2)

# Compute the expression inside the logarithm: 3 - 2*sqrt(2)
inner_expr = 3 - 2 * sqrt2

# Compute the natural logarithm of the inner expression
log_term = mp.log(inner_expr)

# Calculate pi/8
pi_over_8 = mp.pi / 8

# Combine the terms: -log_term - pi_over_8
result = -log_term - pi_over_8

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))