import mpmath as mp

# Set internal decimal precision to 15 for calculations
mp.dps = 15

# Calculate sqrt(3)
sqrt3 = mp.sqrt(3)

# Compute (2 + sqrt(3))
inner_expr = 2 + sqrt3

# Compute ln(2 + sqrt(3))
log_term1 = mp.log(inner_expr)

# Compute (1/2) * ln(3)
log_term2 = 0.5 * mp.log(3)

# Subtract the two terms: ln(2 + sqrt(3)) - (1/2) * ln(3)
result = log_term1 - log_term2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))