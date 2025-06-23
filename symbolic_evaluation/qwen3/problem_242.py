import mpmath as mp
mp.dps = 15  # Set internal precision

# Calculate Gamma(1/3)
gamma_one_third = mp.gamma(mp.mpf(1)/3)

# Compute Gamma(1/3)^6
gamma_term = gamma_one_third ** 6

# Calculate 2^(2/3) using exact exponent
two_power = mp.power(2, mp.mpf(2)/3)

# Compute denominator components
denominator_part = 32 * two_power * mp.pi**2

# Combine all components for final result
result = gamma_term / denominator_part

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))