import mpmath as mp

mp.dps = 15  # Set decimal precision for calculations

# Calculate π/2
pi_over_2 = mp.pi / 2

# Calculate dilogarithm Li₂(1/4)
dilog_value = mp.polylog(2, 0.25)

# Multiply components to get final result
result = pi_over_2 * dilog_value

# Print with 10 decimal precision
print(mp.nstr(result, n=10))