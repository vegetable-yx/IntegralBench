import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Calculate sqrt(2) once for reuse
sqrt2 = mp.sqrt(2)

# Compute first term components
pi_half = mp.pi / 2
sqrt_term = sqrt2 - 1
term1 = pi_half * sqrt_term

# Compute second term components
log_argument = (1 + sqrt2) / 2
log_value = mp.log(log_argument)
term2 = (mp.pi / 4) * log_value

# Combine terms for final result
result = term1 - term2

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))