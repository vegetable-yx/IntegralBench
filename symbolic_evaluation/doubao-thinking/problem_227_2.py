import mpmath as mp

mp.dps = 15  # Set decimal precision for calculations

# Calculate ln(1 + sqrt(2))
sqrt2 = mp.sqrt(2)
log_term = mp.log(1 + sqrt2)

# Square the logarithmic term
log_squared = log_term ** 2

# Compute first term: (π/2) * [ln(1+√2)]²
pi_half = mp.pi / 2
first_term = pi_half * log_squared

# Compute second term: π³/48
pi_cubed = mp.pi ** 3
second_term = pi_cubed / 48

# Combine terms for final result
result = first_term - second_term

# Print result with 10 decimal places
print(mp.nstr(result, n=10))