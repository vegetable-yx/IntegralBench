import mpmath as mp

mp.dps = 15

# Calculate sqrt(24)
sqrt_24 = mp.sqrt(24)

# Compute arguments for Gamma functions
gamma_arg1 = (5 + sqrt_24 + 1) / 2
gamma_arg2 = (5 + sqrt_24 + 2) / 2

# Calculate Gamma values
gamma_numerator = mp.gamma(gamma_arg1)
gamma_denominator = mp.gamma(gamma_arg2)

# Compute components of the expression
sqrt_pi = mp.sqrt(mp.pi)
fraction = gamma_numerator / gamma_denominator

# Combine all components for final result
result = 0.5 * sqrt_pi * fraction

# Print with 10 decimal precision
print(mp.nstr(result, n=10))