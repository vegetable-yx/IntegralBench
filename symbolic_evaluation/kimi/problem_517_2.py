import mpmath as mp
mp.dps = 15  # Set decimal places for internal precision

# Calculate the exponential component e^(1/8)
exponent = mp.mpf(1)/8
e_power = mp.exp(exponent)

# Calculate the square root of (π/2)
pi_over_2 = mp.pi/2
sqrt_pi_over_2 = mp.sqrt(pi_over_2)

# Combine components for final result
result = e_power * sqrt_pi_over_2

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))