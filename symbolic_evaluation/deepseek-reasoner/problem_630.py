import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Compute fundamental constant π
pi_val = mp.pi

# Calculate natural logarithm of 3
ln_3 = mp.log(3)

# Calculate square root of 3
sqrt_3 = mp.sqrt(3)

# Compute numerator: π * ln(3)
numerator = pi_val * ln_3

# Compute denominator: 12 * √3
denominator = 12 * sqrt_3

# Final calculation: (π ln(3)) / (12√3)
result = numerator / denominator

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))