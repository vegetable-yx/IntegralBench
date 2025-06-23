import mpmath as mp

# Set the internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Calculate the trilogarithm term Li_3(1/4)
li3_term = mp.polylog(3, 1/4)

# Calculate the pi/8 coefficient
pi_over_8 = mp.pi / 8

# Multiply components to get the final result
result = pi_over_8 * li3_term

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))