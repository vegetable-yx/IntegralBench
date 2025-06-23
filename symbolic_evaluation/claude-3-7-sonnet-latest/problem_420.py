import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate sqrt(5) once for reuse
sqrt5 = mp.sqrt(5)

# Compute the first term: (3 - sqrt(5)) / 2
term1 = (3 - sqrt5) / 2

# Compute the argument for the logarithm: (-1 + sqrt(5)) / 2
log_arg = (-1 + sqrt5) / 2

# Compute the logarithm term: (1/2) * ln(log_arg)
log_term = 0.5 * mp.log(log_arg)

# Final result: term1 minus log_term
result = term1 - log_term

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))