import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate e^(1/8)
exponent_term = mp.exp(mp.mpf(1)/8)

# Calculate sqrt(pi/2)
sqrt_pi_over_2 = mp.sqrt(mp.pi/2)

# Combine terms for final result
result = exponent_term * sqrt_pi_over_2

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))