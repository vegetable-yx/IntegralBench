import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate Gamma(1/4)
gamma_1_4 = mp.gamma(mp.mpf(1)/4)

# Compute numerator: Gamma(1/4)^4
numerator = gamma_1_4**4

# Calculate denominator components
sqrt2 = mp.sqrt(2)
denominator = 8 * sqrt2 * mp.pi

# Compute final result
result = numerator / denominator

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))