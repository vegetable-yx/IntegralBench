import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate components of the expression separately
sqrt2_plus_1 = 1 + mp.sqrt(2)  # Compute 1 + √2
log_term = mp.log(sqrt2_plus_1)  # Compute natural logarithm of (1 + √2)
pi_half = mp.pi / 2  # Compute π/2

# Multiply the components to get final result
result = pi_half * log_term

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))