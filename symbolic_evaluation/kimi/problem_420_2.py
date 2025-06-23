import mpmath as mp

# Set decimal places for internal precision
mp.dps = 15

# Calculate sqrt(5) once for reuse
sqrt5 = mp.sqrt(5)

# Compute the first term: (1/2) * ln(2*(sqrt(5)-1))
inner_expr = 2 * (sqrt5 - 1)
log_term1 = 0.5 * mp.log(inner_expr)

# Compute the second term: ln(2)
log_term2 = mp.log(2)

# Compute the third term: (-1 + sqrt(5)) / 2
fraction_term = (-1 + sqrt5) / 2

# Combine all terms: log_term1 - log_term2 + fraction_term
result = log_term1 - log_term2 + fraction_term

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))