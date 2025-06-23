import mpmath as mp

# Set the precision to 15 decimal places for calculations
mp.dps = 15

# Calculate the dilogarithm (Spence's function) at 1/4
dilog_value = mp.polylog(2, 1/4)

# Calculate π/2
pi_over_two = mp.pi / 2

# Multiply the results to get the final value
result = pi_over_two * dilog_value

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))