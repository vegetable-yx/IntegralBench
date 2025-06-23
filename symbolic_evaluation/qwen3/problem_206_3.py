import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate sqrt(pi/2)
sqrt_pi_over_2 = mp.sqrt(mp.pi / 2)

# Calculate pi/sqrt(2)
pi_over_sqrt2 = mp.pi / mp.sqrt(2)

# Multiply the two components
result = sqrt_pi_over_2 * pi_over_sqrt2

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))