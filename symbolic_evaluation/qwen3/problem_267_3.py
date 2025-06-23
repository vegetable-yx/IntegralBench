import mpmath as mp
mp.dps = 15  # Set internal decimal precision

# Calculate the trilogarithm term Li_3(1/4)
trilog_value = mp.polylog(3, mp.mpf(1)/4)

# Calculate the pi/8 constant factor
pi_factor = mp.pi / 8

# Combine components for final result
result = pi_factor * trilog_value

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))