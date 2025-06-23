import mpmath as mp

mp.dps = 15  # Set internal precision

# Calculate first term components
sqrt2 = mp.sqrt(2)
log_term = mp.log(1 + sqrt2)  # ln(1 + √2)
squared_log = log_term ** 2  # (ln(1 + √2))^2
term1 = (mp.pi / 8) * squared_log  # π/8 * squared logarithm

# Calculate second term
term2 = (mp.pi - 4) / 16  # (π - 4)/16

# Combine terms for final result
result = term1 + term2

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))