import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate sqrt(5) once and reuse
sqrt5 = mp.sqrt(5)

# Compute first term: (3 - sqrt(5))/2
term1 = (3 - sqrt5) / 2

# Compute the argument for the logarithm: (sqrt(5) + 1)/2
log_arg = (sqrt5 + 1) / 2

# Calculate the logarithmic term: ln((sqrt(5)+1)/2)
log_term = mp.log(log_arg)

# Compute second term: (1/2) * log_term
term2 = 0.5 * log_term

# Sum both terms for final result
result = term1 + term2

# Print result with 10 decimal places
print(mp.nstr(result, n=10))