import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate each component of the integral
term_a = mp.pi**2 / 36
term_b = mp.pi * mp.sqrt(3) / 12
term_c = mp.mpf(1)/4

# Combine terms to compute the integral value
integral_value = term_a - term_b + term_c

# Compute the main expression (π²/72 - integral)
pi_sq_over_72 = mp.pi**2 / 72
result = pi_sq_over_72 - integral_value

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))