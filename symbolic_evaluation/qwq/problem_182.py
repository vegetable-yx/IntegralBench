import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate π/2
pi_over_2 = mp.pi / 2

# Calculate natural logarithm of 2
log2 = mp.log(2)

# First term: (π/2) * ln(2)
term1 = pi_over_2 * log2

# Calculate arctangent of 2
arctan2 = mp.atan(2)

# Square the arctangent result
arctan2_squared = arctan2 ** 2

# Second term: 0.5 * (arctan(2))^2
term2 = 0.5 * arctan2_squared

# Combine terms for final result
result = term1 - term2

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))