import mpmath as mp
mp.dps = 15  # Set internal decimal places for calculations

# Calculate the dilogarithm term Li₂(1/16)
dilog_value = mp.polylog(2, mp.mpf(1)/16)

# Calculate π/2
pi_half = mp.pi / 2

# Multiply components to get final result
result = pi_half * dilog_value

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))