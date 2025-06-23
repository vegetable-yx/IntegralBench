import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Calculate π squared
pi_sq = mp.pi ** 2

# Compute 1 + sqrt(2)
sqrt2_plus_1 = 1 + mp.sqrt(2)

# Calculate natural logarithm term
log_term = mp.log(sqrt2_plus_1)

# Compute first part of the expression: (π²/8) * ln(1+√2)
first_term = (pi_sq / 8) * log_term

# Calculate second part of the expression: (π/4)²
second_term = (mp.pi / 4) ** 2

# Combine terms for final result
result = first_term - second_term

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))