import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate the dilogarithm term Li_2(1/4)
dilog_term = mp.polylog(2, 1/4)

# Calculate π/2
pi_half = mp.pi / 2

# Multiply the components to get final result
result = pi_half * dilog_term

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))