import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Calculate the exponent component 1/8
exponent = mp.mpf(1)/8

# Compute e^(1/8) using mpmath's exp function
exp_term = mp.exp(exponent)

# Calculate the square root of (π/2)
sqrt_pi_over_2 = mp.sqrt(mp.pi/2)

# Combine both components for final result
result = exp_term * sqrt_pi_over_2

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))