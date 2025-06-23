import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate e^(1/8)
exponent = mp.mpf(1)/8
e_term = mp.exp(exponent)

# Calculate sqrt(pi/2)
pi_over_2 = mp.pi / 2
sqrt_pi_half = mp.sqrt(pi_over_2)

# Combine terms for final result
result = e_term * sqrt_pi_half

print(mp.nstr(result, n=10))