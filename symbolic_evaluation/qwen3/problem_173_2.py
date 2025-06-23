import mpmath as mp
mp.dps = 15  # Set decimal precision for intermediate calculations

# Calculate natural logarithm term
ln_term = mp.log(mp.mpf(4)/3)
scaled_ln = 3 * ln_term

# Calculate dilogarithm term
dilog_term = mp.polylog(2, mp.mpf(1)/4)

# Combine all components
sum_components = -1 + scaled_ln + dilog_term

# Multiply by π/8 for final result
result = (mp.pi / 8) * sum_components

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))